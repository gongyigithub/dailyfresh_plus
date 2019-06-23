"""
Django settings for dailyfresh_plus project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd^xh@qx2=%dt+i!p=r=by8gc38p$u=4pqdc1q6xxqa90wk+(uj'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'user',
    'goods',
    'order',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar
]

INTERNAL_IPS = ['192.168.78.134', ]  # 若本机调试，ip添加为127.0.0.1
DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG, }

ROOT_URLCONF = 'dailyfresh_plus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dailyfresh_plus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'192.168.0.106',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'123',
        'NAME':'dailyfresh1',
        'ATOMIC_REQUESTS':True,
    }
}


#redis缓存
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://192.168.0.106:6379/1',
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    }
}
#django使用redis作为session配置
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# 富文本编辑器配置
# TINYMCE_DEFAULT_CONFIG = {
#     'theme': 'advanced',
#     'width': 600,
#     'height': 400,
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'    #调用时的路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')                   #具体路径
]
from django.conf import settings

#邮件加密密钥
EMAIL_KEY = 'ASDFG'

#发送邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#smtp服务地址
EMAIL_HOST = 'smtp.sina.com'
#端口号
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'gxylogin@sina.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'ko433844xlyx'
#收件人看到的发件人
EMAIL_FROM = '天天生鲜<gxylogin@sina.com>'

#日志模块
from logging.handlers import SysLogHandler
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standward':{
            'format':'%(asctime)s[%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s:%(message)s]',
        },
    },
    'filters':{  #过滤器
        'require_debug_false':{
            '()':'django.utils.log.RequireDebugFalse',
        }
    },

    'handlers':{  #处理器
        'null':{
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'mail_admin':{  #发送邮件
            'level':'ERROR',
            'class':'django.utils.log.AdminEmailHandler',
            'filters':['require_debug_false'],  #仅当DEBUG=false时才发送邮件.这里引用的是上边那个filters
            'include_html':True
        },
        'debug':{  #记录到日志文件
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'encoding':'utf-8',
            'filename':os.path.join(BASE_DIR,'log','debug.log'),#日志输出文件
            'maxBytes':1024*1024*5, #文件大小
            'backupCount':2,  #备份份数
            'formatter':'standward',  #使用的日志格式
        },
        'console':{#输出到控制台
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'standward'
        },
    },

    'loggers':{#logging管理器..这里采用了三种日志记录方式，分别是django---将日志信息输出到文件，django.request---将信息输出到控制台
        'django_file':{
            'handlers':['console'],
            'level':'DEBUG',
            'propagate':False
        },
        'django_console':{
            'handlers':['debug'],
            'level':'INFO',
            'propagate':True,
         },
        #对于不在ALLOWED_HOSTS中的请求不发送邮件
        'django.security.DisallowedHost':{
            'handlers':['null'],
            'propagate':False,
        }
     }
}





