#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Huu' 

import re,time,json,logging,hashlib,base64,asyncio
from coroweb import get,post
from models import User,Comment,Blog,next_id

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