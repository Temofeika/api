# cython:language_level=3
from django.db import models
from django.contrib import admin


class RustDeskToken(models.Model):
    ''' Token
    '''
    username = models.CharField(verbose_name='Имя пользователя', max_length=20)
    rid = models.CharField(verbose_name='TeamDesk ID', max_length=16)
    uid = models.CharField(verbose_name='ID пользователя', max_length=16)
    uuid = models.CharField(verbose_name='uuid', max_length=60)
    access_token = models.CharField(verbose_name='access_token', max_length=60, blank=True)
    create_time = models.DateTimeField(verbose_name='Время входа', auto_now_add=True)
    #expire_time = models.DateTimeField(verbose_name='Срок действия')
    class Meta:
        ordering = ('-username',)
        verbose_name = "Token"
        verbose_name_plural = "Token列表" 

class RustDeskTokenAdmin(admin.ModelAdmin):
    list_display = ('username', 'uid')
    search_fields = ('username', 'uid')
    list_filter = ('create_time', ) #过滤器
    

class RustDeskTag(models.Model):
    ''' Tags
    '''
    uid = models.CharField(verbose_name='ID пользователя', max_length=16)
    tag_name = models.CharField(verbose_name='Название тэга', max_length=60)
    tag_color = models.CharField(verbose_name='Цвет этикетки', max_length=60, blank=True)
    
    class Meta:
        ordering = ('-uid',)
        verbose_name = "Tags"
        verbose_name_plural = "Tags"

class RustDeskTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'uid', 'tag_color')
    search_fields = ('tag_name', 'uid')
    list_filter = ('uid', )
    

class RustDeskPeer(models.Model):
    ''' Pees
    '''
    uid = models.CharField(verbose_name='ID пользователя', max_length=16)
    rid = models.CharField(verbose_name='ID клиента', max_length=60)
    username = models.CharField(verbose_name='Имя пользователя системы', max_length=20)
    hostname = models.CharField(verbose_name='Название операционной системы', max_length=30)
    alias = models.CharField(verbose_name='Псевдоним', max_length=30)
    platform = models.CharField(verbose_name='Платформа', max_length=30)
    tags = models.CharField(verbose_name='Этикетка', max_length=30)
    rhash = models.CharField(verbose_name='Пароль для связи с устройством', max_length=60)
    
    class Meta:
        ordering = ('-username',)
        verbose_name = "Peers"
        verbose_name_plural = "Peers" 
        

class RustDeskPeerAdmin(admin.ModelAdmin):
    list_display = ('rid', 'uid', 'username', 'hostname', 'platform', 'alias', 'tags')
    search_fields = ('deviceid', 'alias')
    list_filter = ('rid', 'uid', )
    
    
class RustDesDevice(models.Model):
    rid = models.CharField(verbose_name='ID клиента', max_length=60, blank=True)
    cpu = models.CharField(verbose_name='CPU', max_length=20)
    hostname = models.CharField(verbose_name='Имя процессора', max_length=20)
    memory = models.CharField(verbose_name='Память', max_length=20)
    os = models.CharField(verbose_name='Операционная система', max_length=20)
    uuid = models.CharField(verbose_name='uuid', max_length=60)
    username = models.CharField(verbose_name='Имя пользователя системы', max_length=60, blank=True)
    version = models.CharField(verbose_name='клиентская версия', max_length=20)
    create_time = models.DateTimeField(verbose_name='Время регистрации устройства', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='Время обновления устройства', auto_now=True, blank=True)
    
    class Meta:
        ordering = ('-rid',)
        verbose_name = "оборудование"
        verbose_name_plural = "Список устройств" 
    
class RustDesDeviceAdmin(admin.ModelAdmin):
    list_display = ('rid', 'hostname', 'memory', 'uuid', 'version', 'create_time', 'update_time')
    search_fields = ('hostname', 'memory')
    list_filter = ('rid', )



class ShareLink(models.Model):
    ''' 分享链接
    '''
    uid = models.CharField(verbose_name='ID пользователя', max_length=16)
    shash = models.CharField(verbose_name='LinkKey', max_length=60)
    peers = models.CharField(verbose_name='Список идентификаторов машин', max_length=20)
    is_used = models.BooleanField(verbose_name='использовать или нет', default=False)
    is_expired = models.BooleanField(verbose_name='Срок годности истек?', default=False)
    create_time = models.DateTimeField(verbose_name='Время генерации', auto_now_add=True)
    

    
    class Meta:
        ordering = ('-create_time',)
        verbose_name = "Поделиться ссылкой"
        verbose_name_plural = "Связанный список" 
        

class ShareLinkAdmin(admin.ModelAdmin):
    list_display = ('shash', 'uid', 'peers', 'is_used', 'is_expired', 'create_time')
    search_fields = ('peers', )
    list_filter = ('is_used', 'uid', 'is_expired' )
