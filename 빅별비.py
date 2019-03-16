import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')
    await client.change_presence(game=discord.Game(name='현존하는 최고인공지능'))

@client.event
async def on_message(message):
    if message.content.startswith('!안녕빅별비'):
        await client.send_message(message.channel, "안녕하세요")
    if message.content.startswith('!빅별비어딨니?'):
        await client.send_message(message.channel, "저 여깄죠")
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, "1.!안녕빅별비 2.!빅별비어딨니? 3. !빅별비명령어 4. !빅별회사 5. !빅별비란 6. !빅별비업데이 7. !빅별비니주인은?")
    if message.content.startswith('!빅별회사'):
        await client.send_message(message.channel, "빅별회사: 회장:빅별한기 공동회장:스팅키 사장: SKY14261 직원: 빅별비,빅별시리 빅별회사는 0.00001nm 기술을 가지고있는 가상속 대기업이다.")
    if message.content.startswith('!빅별비란'):
        await client.send_message(message.channel, "저는 빅별한기 회장님에 의해 만들어진 인공지능입니다.")
    if message.content.startswith('!빅별비업데이트'):
        await client.send_message(message.channel, "아직 최신버전입니다. 현재버전:3.1.2")
    if message.content.startswith('!빅별비니주인은?'):
        await client.send_message(message.channel, "저를 실행시킬경우에는 스팅키회장님이 저의 주인이시고 실행 안하셨을떄는 빅별한기 회장님이 주인입니다. 한마디로 회장님들이 저의 주인입니다")


client.run('NTU0MjA4NTEyMzA2MDUzMTIw.D2ZVNA.pkbXoYOX1rNfz2eqSbdn8YpTJks')
