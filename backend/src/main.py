from graph.workflow import build_workflow
import time
from utils.config import ENTIRE_PRODUCTION_BELT_TIME,BATCH_PRODUCTION_TIME


def main():
    app = build_workflow()

    initial_state = {
        "start_time": time.time(),
        "time_elapsed": 0,# get the current time of production
        "date_time": "",#batch_id
        "batch_ids":[],#need to extract when searching for logs in report generation
        "inventory_data": [],
        "low_stock_items": [],
        "restock_orders": {},
        "is_production_possible": False,#check if production is possible meaning items available for production
        "defects_checked": False,#check if defects are checked
        "defective_items": [],
        "sent_notifications_low_stock_items": [],
        "sent_notifications_low_stock_items_urgent": [],
        "can_report_be_generated": False,#check if report can be generated
        "report_generated": False#check if report is generated
    }

    print("\n>> 🏭 STARTING PRODUCTION BELT...")
    
    while True:
        final_state = app.invoke(initial_state)
        
        print("\n ✅ BATCH SUMMARY ")
        print(f"- Low stock items: {len(final_state['low_stock_items'])}")
        print(f"✔️ Notifications for low stock sent: {len(final_state['sent_notifications_low_stock_items'])}")
        print(f"✔️ Notifications Urgent low stock sent: {len(final_state['sent_notifications_low_stock_items_urgent'])}")
        print(f"⏳ Time elapsed: {final_state['time_elapsed']:.2f} seconds")
        print("\n🟢 ✅ BATCH PROCESS COMPLETED! ")
        
        if final_state['report_generated']:
            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"\n🏁 🎯 COMPLETED PRODUCTION BELT...")
            print(f"⏳ TOTAL TIME TAKEN: {final_state['time_elapsed']:.2f} seconds")
            break


if __name__ == "__main__":
    main()
 