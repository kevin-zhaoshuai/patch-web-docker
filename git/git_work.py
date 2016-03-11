# -*- coding: utf-8 -*-
# created by Shuai.Zhao Apr.2015

import re
import os,sched
import subprocess
import sys
import MySQLdb
import time,datetime
import types

#Read from os env
dbAddr = os.environ.get('MYSITE_DB_1_PORT_3306_TCP_ADDR')

#Port needs to be an interger
dbPort = os.environ.get('MYSITE_DB_1_PORT_3306_TCP_PORT')
dbPort = int(dbPort)

dbPasswd = os.environ.get('MYSITE_DB_1_ENV_MYSQL_ROOT_PASSWORD')
dbDatabase = os.environ.get('MYSITE_DB_1_ENV_MYSQL_DATABASE')

schedule = sched.scheduler(time.time,time.sleep)

def run(tablename,project_dir, date_from, date_to, search_key,mail_list,name_list):
    bug_dic = {}
    bug_branch_dic = {}
    try:
        os.chdir(project_dir)
    except Exception, e:
        raise e
    cmd = "git pull"
    os.system(cmd)

    check_all(tablename,mail_list,name_list)
 
# check for all the people in the list
def check_all(tabelname,mail_list,name_list):
    listLenMail = len(mail_list)
    listLenName = len(name_list)
    count = 0
    if listLenMail != listLenName :
        print "Maillist and namelist length do not match"

    for name in name_list:
        get_commit_nums(tabelname,mail_list[count],name)
        count = count+1
	
# get the number of commits
def get_commit_nums(tablename,mail,name):
    cmd_git_nums = 'git log --author=\"'+mail+'\" --pretty=format:\"%h %an %ae %ci   %s. \"'
    print cmd_git_nums
    proc = subprocess.Popen(cmd_git_nums,shell=True,stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
	match_hash = re.search("\w+",line)
	if match_hash :
	    user_hash = match_hash.group()
            print user_hash
	    
	else:
	    print("Can not match hash")

	match_name = re.search(name, line)
	if match_name :
	    user_name = match_name.group()
            print user_name
	    
	else:
	    print("Can not match name")

#	match_email = re.search('\S*@linux.vnet.ibm.com',line)
#	if match_email:
#	    user_email = match_email.group()
#	    print user_email    
#	else:
#	    print("Can not match useremail")
	user_email = " "

#	Time format    :            2013-05-20 13:14:52
	match_committime = re.search(r'\w+-\w+-\w+ \w+:\w+:\w+',line)
	if match_committime:
	    user_committime = match_committime.group()
	    print user_committime
	else:
	    print("Can not match committime")
	
	match_comment = re.search(r'  .*\. ',line)
	if match_comment:
	    user_comment = match_comment.group()
	    print user_comment
	else:
	    print("Can not match comment")
	if match_name and match_committime and match_comment and match_hash:
            print("Match complete")
	    put_into_mysql(tablename,user_name,user_email,user_committime,user_comment,user_hash)
	
def put_into_mysql(tablename,name,email,committime,comment,hash):
	conn= MySQLdb.connect(
			host= dbAddr,
			port = dbPort,
			user = 'root',
			passwd = dbPasswd,
			db = dbDatabase,
			)
	cur = conn.cursor()
	print 'Ongoing writing to the database'
#        time_datetime = datetime.datetime.strptime(committime,'%Y-%m-%d %H:%M:%S')
#	print type(time_datetime)
#	print time_datetime
	sqli="insert into "+tablename+" values(%s,%s,%s,%s,%s,%s)"
	cur.execute(sqli,('0',name,email,committime,comment,hash))	
	cur.close()
	conn.commit()
	conn.close()

def mysql_init(tablename):
	conn= MySQLdb.connect(
			host= dbAddr,
			port = dbPort,
			user = 'root',
			passwd = dbPasswd,
			db = dbDatabase,
			)
	cur = conn.cursor()
	cur.execute("truncate table "+tablename)
	print 'Flush table success:'+tablename
	cur.close()
	conn.commit()
	conn.close()

# analyze log 
def deal_lines(date_from, date_to, search_key, stdout):
    for line in stdout.split('commit '):
        if re.search('Bug: \d+', line) is not None and re.search(search_key, line) is not None:
            bug_id = line.split('Bug: ')[1].split('\n')[0]
            if bug_id not in bug_dic:
                bug_dic[bug_id] = [line]
            else:
                bug_dic[bug_id] += [line]
    return bug_dic

#   update datebase
def update_database0(para1,para2,inc):
    tablename1="commitinfo_kernel_project"
    project_dir1 = "/code/linux/"

    name_list1 = ['Li Zhong','Wei Yang','Jia He','Boqun Feng','Boqun Feng','Xiao Guangrong','Mike Qiu','Guo Chao','Zhi Yong Wu','Cong Meng','Li Zhang']
    mail_list1 = ['zhong@linux.vnet.ibm.com','weiyang@linux.vnet.ibm.com','hejianet@gmail.com','boqun.feng@gmail.com','boqun.feng@linux.vnet.ibm.com','xiaoguangrong@linux.vnet.ibm.com','qiudayu@linux.vnet.ibm.com','yan@linux.vnet.ibm.com','wuzhy@linux.vnet.ibm.com','mc@linux.vnet.ibm.com','zhlcindy@gmail.com']
    mysql_init(tablename1)
    run(tablename1,project_dir1, date_from, date_to, search_key,mail_list1,name_list1)
    
    name_list2 = ['Li Zhang','Li Zhang']
    mail_list2 = ['zhlcindy@gmail.com','zhlcindy@linux.vnet.ibm.com']
    project_dir2="/code/libvirt"
    tablename2="commitinfo_libvirt_project"
    mysql_init(tablename2)
    run(tablename2,project_dir2, date_from, date_to, search_key,mail_list2,name_list2)
    
    name_list3 = ['parklong','park hei','park hei','Wen Zhi Yu','Wen Zhi Yu']
    mail_list3 = ['heijlong@linux.vnet.ibm.com','heijlong@linux.vnet.ibm.com','jianlonghei@gmail.com','wenzhi_yu@163.com','yuywz@cn.ibm.com']
    project_dir3="/code/nova"
    tablename3="commitinfo_openstack_project"
    mysql_init(tablename3)
    run(tablename3,project_dir3, date_from, date_to, search_key,mail_list3,name_list3)

def begin_running(inc=86400):
    schedule.enter(inc,0,update_database0,(0,0,inc))
    schedule.run()

if __name__ == '__main__':
    date_from = "20**-**-**"
    date_to = "****-**-**"
    search_key = "Bug:\d"
    update_database0(0,0,0)
    begin_running()

