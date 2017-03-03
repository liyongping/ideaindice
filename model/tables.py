#-*-coding:utf-8-*-

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.engine import reflection
from sqlalchemy import Column, Integer, SmallInteger, String, Date, Time,\
    Text, DateTime, create_engine, func, Table
from sqlalchemy.ext.declarative import declarative_base

from settings import DB_CONNECT_STRING, DB_ENCODING, DB_ECHO, POOL_RECYCLE

engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO)
# 为了解决mysql gone away尝试使用NullPool和设置POOL_RECYCLE为5s
#engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO, pool_recycle=POOL_RECYCLE, poolclass=NullPool)

Base = declarative_base()

class Function(Base):
    """
	功能模块表
    """
    __tablename__ = 'function'
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    # 功能名称
    name = Column(String(32), unique=True, nullable=False)
    # 功能描述
    desc = Column(Text, nullable=False)

class Role(Base):
    """
	角色表
    """
    __tablename__ = 'role'
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True, nullable=False)
    desc = Column(Text, nullable=False)

class Role_Func(Base):
    """
	角色功能对应表
    """
    __tablename__ = 'function'
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    roleid = Column(Integer(11), default=0, nullable=False)
    funcid = Column(Integer(11), default=0, nullable=False)

class User_Role(Base):
    """
	用户角色对应表
    """
    __tablename__ = 'function'
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    userid = Column(Integer(11), default=0, nullable=False)
    roleid = Column(Integer(11), default=0, nullable=False)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer(11), primary_key=True, autoincrement=True)
    # 登录名
    loginname = Column(String(32), unique=True, nullable=False)
    # 昵称
    nickname = Column(String(32), nullable=False)
    _password = Column('password', String(64), default='', nullable=False)
    # email为唯一，即一个邮箱只可以注册一个用户，也可以通过邮箱进行登录
    email = Column(String(250), unique=True, default='')
    # 用户主页
    url = Column(String(250), default='')
    # 注册时间
    registered = Column(DateTime(), default=func.now(), nullable=False)
    '''
    status: 
    0-新注册  1-已激活  2-封杀
    '''
    status = Column(Integer(1), default='0', nullable=False)
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        import hashlib
        # encrypt the password with md5
        self._password = unicode(hashlib.md5(password).hexdigest(),'utf-8')
class UserInfo(Base):
    __tablename__ = 'userinfo'
    # 会员头像
    avatar = Column(String(255), default='')
    # 性别：0为女 ，1为男，2为未知
    gender = Column(Integer(1), default='2')
    # 手机号码
    mobile = Column(String(32), default='')
    # qq号码
    qq = Column(String(32), default='')
    # 账户余额
    money = Column(Integer(11), default='')
    # 账户积分
    score = Column(Integer(11), default='')
    # 邮政编码
    zipcode = Column(String(16), default='')
    # 联系地址
    address = Column(String(256), default='')
    # 所在城市ID
    cityid = Column(Integer(11), default='')

class UserMeta(Base):
    __tablename__ = 'usermeta'
    
    metaid = Column(Integer(11), primary_key=True, autoincrement=True)
    userid = Column(Integer(11), default=0, nullable=False)
    key = Column(String(255), default='', nullable=False)
    value = Column(Text, nullable=False)
