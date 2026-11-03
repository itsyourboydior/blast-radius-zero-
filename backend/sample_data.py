"""
Preloaded sample datasets showcasing real-world Vultr cloud analytics and security audits.
"""
import os
import csv
import random

SAMPLE_VULTR_METRICS = """timestamp,instance_id,region,vcpu,ram_gb,cpu_util_pct,mem_util_pct,tx_mbps,rx_mbps,cost_hourly,status
2026-11-03 00:00:00,vultr-vm-01,EWR (New Jersey),4,16,42.5,58.2,120.4,310.2,0.048,active
2026-11-03 01:00:00,vultr-vm-01,EWR (New Jersey),4,16,68.9,71.0,240.1,512.6,0.048,active
2026-11-03 02:00:00,vultr-vm-01,EWR (New Jersey),4,16,91.4,86.5,410.8,820.5,0.048,active
2026-11-03 03:00:00,vultr-vm-01,EWR (New Jersey),4,16,84.2,82.1,380.0,790.3,0.048,active
2026-11-03 00:00:00,vultr-vm-02,FRA (Frankfurt),8,32,35.1,44.0,95.0,210.0,0.096,active
2026-11-03 01:00:00,vultr-vm-02,FRA (Frankfurt),8,32,48.6,52.3,180.2,400.1,0.096,active
2026-11-03 02:00:00,vultr-vm-02,FRA (Frankfurt),8,32,77.3,79.8,320.5,650.0,0.096,active
2026-11-03 03:00:00,vultr-vm-02,FRA (Frankfurt),8,32,88.9,85.2,390.0,710.4,0.096,active
2026-11-03 00:00:00,vultr-vm-03,NRT (Tokyo),2,8,22.0,30.5,45.2,110.0,0.024,active
2026-11-03 01:00:00,vultr-vm-03,NRT (Tokyo),2,8,38.4,41.2,88.0,195.4,0.024,active
2026-11-03 02:00:00,vultr-vm-03,NRT (Tokyo),2,8,55.1,59.0,140.2,305.8,0.024,active
2026-11-03 03:00:00,vultr-vm-03,NRT (Tokyo),2,8,61.7,64.3,165.0,340.1,0.024,active
2026-11-03 00:00:00,vultr-vm-04,SJC (Silicon Valley),16,64,65.3,60.1,450.0,920.0,0.192,active
2026-11-03 01:00:00,vultr-vm-04,SJC (Silicon Valley),16,64,82.4,78.5,680.1,1350.2,0.192,active
2026-11-03 02:00:00,vultr-vm-04,SJC (Silicon Valley),16,64,96.8,92.1,890.4,1780.0,0.192,active
2026-11-03 03:00:00,vultr-vm-04,SJC (Silicon Valley),16,64,93.2,89.4,810.0,1620.5,0.192,active
2026-11-03 00:00:00,vultr-vm-05,LHR (London),4,16,18.5,25.0,40.1,95.0,0.048,active
2026-11-03 01:00:00,vultr-vm-05,LHR (London),4,16,29.1,33.2,65.4,140.0,0.048,active
2026-11-03 02:00:00,vultr-vm-05,LHR (London),4,16,51.8,55.0,110.2,250.7,0.048,active
2026-11-03 03:00:00,vultr-vm-05,LHR (London),4,16,73.4,70.2,190.5,410.2,0.048,active
"""

SAMPLE_FINANCIAL_CHURN = """customer_id,plan_tier,monthly_revenue_usd,tenure_months,support_tickets,nps_score,storage_gb,churned
CUST-1001,Enterprise,1250,28,1,9,4500,0
CUST-1002,Pro,240,14,3,8,820,0
CUST-1003,Starter,49,4,7,4,110,1
CUST-1004,Starter,49,2,9,3,85,1
CUST-1005,Enterprise,1800,36,0,10,9200,0
CUST-1006,Pro,320,18,2,7,1150,0
CUST-1007,Pro,240,6,8,5,420,1
CUST-1008,Enterprise,2100,42,2,9,12400,0
CUST-1009,Starter,49,1,6,2,40,1
CUST-1010,Pro,390,22,1,8,1600,0
CUST-1011,Starter,49,8,3,7,210,0
CUST-1012,Enterprise,1500,19,4,6,6100,0
CUST-1013,Pro,290,11,5,5,780,1
CUST-1014,Enterprise,3200,50,1,10,18500,0
CUST-1015,Starter,49,3,8,3,95,1
"""

def seed_sample_data(base_dir: str):
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    file_vultr = os.path.join(data_dir, "vultr_cloud_compute_metrics.csv")
    with open(file_vultr, "w", encoding="utf-8") as f:
        f.write(SAMPLE_VULTR_METRICS.strip())
        
    file_churn = os.path.join(data_dir, "saas_churn_financials.csv")
    with open(file_churn, "w", encoding="utf-8") as f:
        f.write(SAMPLE_FINANCIAL_CHURN.strip())
        
    return {
        "vultr_metrics": file_vultr,
        "saas_churn": file_churn
    }
