import orm,asyncio
from models import User, Blog, Comment

loop=asyncio.get_event_loop()
async def test():
    
    u = User(name='huf', email='111@qq.com', passwd='3242352453', image='about:blank')
    await u.save()
    # u=await User.find('1')
    # print(u)
    

loop.run_until_complete(orm.create_pool(loop,user='www-data',password='www-data',db='awesome'))
loop.run_until_complete(test())
loop.run_forever()