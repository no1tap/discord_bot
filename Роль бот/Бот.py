import discord
from discord import utils



import config
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Бот підключин  {0}!'.format(self.user))
 
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) 
            message = await channel.fetch_message(payload.message_id) 
            member = payload.member
            print(member)
            try:
                emoji = str(payload.emoji) 
                role = utils.get(message.guild.roles, id=config.ROLES[emoji]) 
            
                if(len([i for i in member.roles if i and i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('Користувач {0.display_name} отримав роль {1.name}'.format(member, role))
                
                    
            
            except KeyError as e:
                print('Помилка не задано роль для ' + emoji)
            except Exception as e:
                print(repr(e))
                
 
    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id) 
        message = await channel.fetch_message(payload.message_id)
        user_id=payload.user_id
        member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id) 
        print(member, user_id)
 
        try:
            emoji = str(payload.emoji) 
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]) 
 
            await member.remove_roles(role)
            print(' {1.name} була видалена  для {0.display_name}'.format(member, role))
 
        except KeyError as e:
            print('Помилка не задано роль для ' + emoji)
        except Exception as e:
            print(repr(e))
 

client = MyClient()
client.run(config.TOKEN)
