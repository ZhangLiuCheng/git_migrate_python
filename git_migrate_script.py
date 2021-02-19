#coding=utf-8
from git import Repo
import git
import os
# rep_list  =  ["ssh://git@119.29.247.107:10022/zhangliucheng/coupon.git",
#               'ssh://git@119.29.247.107:10022/zhangliucheng/coupon_java.git',
#               "ssh://git@119.29.247.107:10022/zhangliucheng/shop.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/ShopH5.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/prds.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/ReptileIdiom.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/movie.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/ReptileVideo.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/film.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/book.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/Encrypt.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/PlayIN.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/WaWaJi.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/MobileServer.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/attributed.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/interview.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/flutter_plugin_taobao.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/flutter_weixin.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/qtt_web_tool.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/animal.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/Identify.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/wish.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/rollingball.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/babyGame.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/Archer.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/tarot.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/faceGrade.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/fill_wx.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/defend-tang.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/fur_heidong.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/idiom_wx.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/ball.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/circle.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/fotomix.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/Math.git",
#               "ssh://git@119.29.247.107:10022/zhangliucheng/Rapid.git"]

rep_list  =  ['ssh://git@119.29.247.107:10022/sunyuqin/fill_java.git',
              "ssh://git@119.29.247.107:10022/sunyuqin/mom.git",
              "ssh://git@119.29.247.107:10022/sunyuqin/identify_java.git",
              "ssh://git@119.29.247.107:10022/sunyuqin/quanzi.git"]

path = 'GitSource'
for i in rep_list:
    #从列表中获取每个项目的项目名称，并创建对应文件夹
    folder = i.split('/',-1)[4]
    print(folder)
    folder_name = '/'+folder
    gitPath = path+folder_name
    os.mkdir(gitPath)
    Repo.clone_from(url=i, to_path=path+folder_name)
 
    #获取远程分支的分支名称
    repo = git.Repo(path+folder_name)
    remote_branches = []
    for ref in repo.git.branch('-r').split('\n'):
        remote_branches.append(ref)
    print(remote_branches)
    del remote_branches[0]
    print(remote_branches)
 
    #获取分支名称
    bran_name = []
    for bran in remote_branches:
        print(bran.split('/', 1)[1])
        bran_name.append(bran.split('/', 1)[1])
    print(bran_name)
 
    #在本地切换一遍分支，因为在上传至新的gitlab库时，只会把已存在的本地分支上传，没有的不会上传，所以必须把所有分支都切换一遍
    for bran in bran_name:
        repo.git.checkout(bran)