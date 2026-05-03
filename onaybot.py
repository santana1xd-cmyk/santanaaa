import discord
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# ============================================
# BOT AYARLARI (Environment Variables'dan)
# ============================================
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID', 0))
REMOVE_LOG_CHANNEL_ID = int(os.getenv('REMOVE_LOG_CHANNEL_ID', 0))
ROLE_ID = int(os.getenv('ROLE_ID', 0))
# ============================================

# Bot ayarları
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Kontrol edilen kullanıcıları takip et (spam önleme)
checked_users = set()

@bot.event
async def on_ready():
    print(f'✅ Bot aktif: {bot.user.name}')
    print(f'📊 {len(bot.guilds)} sunucuda aktif')

@bot.event
async def on_presence_update(before, after):
    try:
        # Bot ise çık
        if after.bot:
            return
        
        member = after
        
        # Önceki ve yeni custom status'leri bul
        old_custom_status = None
        new_custom_status = None
        
        if before:
            for activity in before.activities:
                if isinstance(activity, discord.CustomActivity):
                    old_custom_status = activity
                    break
        
        for activity in after.activities:
            if isinstance(activity, discord.CustomActivity):
                new_custom_status = activity
                break
        
        # Önceki durumda discord.gg/onay var mıydı?
        had_onay = False
        if old_custom_status and old_custom_status.name:
            had_onay = 'discord.gg/onay' in old_custom_status.name.lower()
        
        # Yeni durumda discord.gg/onay var mı?
        has_onay = False
        if new_custom_status and new_custom_status.name:
            has_onay = 'discord.gg/onay' in new_custom_status.name.lower()
        
        role = member.guild.get_role(ROLE_ID)
        
        # DURUM 1: Yeni ekledi (önceden yoktu, şimdi var)
        if not had_onay and has_onay:
            print(f'✅ Eklendi: {member.name} - "{new_custom_status.name}"')
            checked_users.add(member.id)
            
            # Ekleme logu için ayrı kanal
            log_channel = bot.get_channel(LOG_CHANNEL_ID)
            if log_channel:
                embed = discord.Embed(
                    title='✅ Yeni Onay Tespit Edildi',
                    description=f'{member.mention} Durumuna **discord.gg/onay** Yazdı!',
                    color=0x00ff00,
                    timestamp=datetime.utcnow()
                )
                embed.add_field(name='👤 Kullanıcı', value=f'{member.name}#{member.discriminator}', inline=True)
                embed.add_field(name='🆔 ID', value=str(member.id), inline=True)
                embed.add_field(name='📝 Durum Mesajı', value=f'`{new_custom_status.name}`', inline=False)
                embed.set_thumbnail(url=member.display_avatar.url)
                embed.set_footer(text='Onay Bot')
                
                await log_channel.send(embed=embed)
            
            # Rol ver
            if role and role not in member.roles:
                await member.add_roles(role)
                print(f'✅ {member.name} Kullanıcısına Rol Verildi')
                
                try:
                    await member.send(f'🎉 **Tebrikler! Discord Durumuna **discord.gg/onay** Yazdığın İçin {role.name} Rolünü Aldın!** ')
                except:
                    print(f'❌ {member.name} Kullanıcısına DM Gönderilemedi')
        
        # DURUM 2: Kaldırdı (önceden vardı, şimdi yok)
        elif had_onay and not has_onay:
            print(f'❌ Kaldırıldı: {member.name}')
            checked_users.discard(member.id)
            
            # Kaldırma logu için ayrı kanal
            remove_log_channel = bot.get_channel(REMOVE_LOG_CHANNEL_ID)
            if remove_log_channel:
                # Yeni durum mesajını al (varsa)
                new_status_text = "Durum silindi"
                if new_custom_status and new_custom_status.name:
                    new_status_text = new_custom_status.name
                
                embed = discord.Embed(
                    title='❌ Onay Durumu Kaldırıldı',
                    description=f'{member.mention} Durumundan **discord.gg/onay** Kaldırdı!',
                    color=0xff0000,
                    timestamp=datetime.utcnow()
                )
                embed.add_field(name='👤 Kullanıcı', value=f'{member.name}#{member.discriminator}', inline=True)
                embed.add_field(name='🆔 ID', value=str(member.id), inline=True)
                embed.add_field(name='📝 Yeni Durum', value=f'`{new_status_text}`', inline=False)
                embed.set_thumbnail(url=member.display_avatar.url)
                embed.set_footer(text='Onay Bot')
                
                await remove_log_channel.send(embed=embed)
            
            # Rolü geri al
            if role and role in member.roles:
                await member.remove_roles(role)
                print(f'🔴 {member.name} Kullanıcısından Rol Geri Alındı')
                
                try:
                    await member.send(f'⚠️ **Discord Durumundan **discord.gg/onay** Kaldırdığın İçin {role.name} Rolün Geri Alındı!** ')
                except:
                    print(f'❌ {member.name} Kullanıcısına DM Gönderilemedi')
                
    except Exception as e:
        print(f'❌ Hata: {e}')

# Bot'u başlat
bot.run(DISCORD_TOKEN)
