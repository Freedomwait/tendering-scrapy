# 1. 运行 notice spider
# 2. 运行 price spider
# 2. 运行 contract spider
# 3. 运行 mergeexcel 脚本
# 4. finish 推送邮件通知
# 5. 推送飞书通知
#
echo "===== start task ====="

echo "===== start crawl notice ====="

scrapy crawl notice

echo "===== finish crawl notice ====="


echo "===== start crawl price ====="

scrapy crawl price

echo "===== finish crawl price ====="


echo "===== start crawl contract ====="

scrapy crawl contract

echo "===== finish crawl contract ====="


echo "===== start merge excel file ====="

python mergeexcel.py

echo "===== finish merge excel file ====="


echo "===== start sending email ====="

python sendeamil.py

echo "===== finish sending email ====="


echo "===== send feishu bot notice ====="

python webhook.py

echo "===== success sending feishu bot notice ====="


echo "===== finish task ====="
