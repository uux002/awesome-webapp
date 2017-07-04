__author__ = "FredShao"

import asyncio, logging
import aiomysql

def log(sql,args=()):
    logging.info('SQL: %s' % sql)

async def create_pool(loop,**kw):
    logging.info('create database connection pool...')