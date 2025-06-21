from crawler.task_fetch_104_data import fetch_104_data

# task_2330 = crawler_finmind.s(stock_id="2330")
# task_2330.apply_async(queue="twse")  # 發送任務
# print("send task_2330 task")

job_url = "https://www.104.com.tw/job/7anso?jobsource=google"
fetch_104 = fetch_104_data.s(job_url)
fetch_104.apply_async(queue="104")
print("send task_104 task")

