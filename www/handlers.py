#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Huu' 

import re,time,json,logging,hashlib,base64,asyncio
import markdown2
from aiohttp import web
from coroweb import get,post
from models import User,Comment,Blog,next_id
from apis import APIValueError,APIResourseNotFoundError
from config import configs

COOKIE_NAME='awesession'
_COOKIE_KEY=configs.session.secret

def user2cookie(user,max_age):
    expires=str(int(time.time()+max_age))
    #built cookie string by:id-expires-sha1
    s='%s-%s-%s-%s'%(user.id,user.passwd,expires,_COOKIE_KEY)
    L=[user.id,expires,hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


@get('/')
async def index(request):
    summary='sadasfsdgjh asdjasl asd jalij asd aiohjsda;iofh asdfh ;aioha '
    blogs=[
        Blog(id=1,name='TEST BLOGS',summary=summary,created_at=time.time()-120),
        Blog(id=2,name='second BLOGS',summary=summary,created_at=time.time()-120),
        Blog(id=3,name='last BLOGS',summary=summary,created_at=time.time()-120)
    ]
    return{
        '__template__':'blogs.html',
        'blogs':blogs
    }

@get('/api/users')
async def api_get_users():
    users=await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd='******'
    return dict(users=users)