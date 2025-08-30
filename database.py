from supabase import create_client
from datetime import datetime, timedelta
import os

try:
    SUPABASE_URL = os.environ["SUPABASE_URL"]
    SUPABASE_KEY = os.environ["SUPABASE_KEY"]
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    print("❌ Supabase client failed to initialize:", e)
    raise

def log_alert(ticker, tier, score=None):
    try:
        supabase.table("alerts").insert({
            "ticker": ticker,
            "tier": tier,
            "score": score,
            "timestamp": datetime.utcnow().isoformat()
        }).execute()
    except Exception as e:
        print(f"❌ Failed to log alert for {ticker}: {e}")

def check_recent_alerts(ticker):
    try:
        recent = (datetime.utcnow() - timedelta(hours=6)).isoformat()
        result = supabase.table("alerts").select("ticker").eq("ticker", ticker).gte("timestamp", recent).execute()
        return len(result.data) > 0
    except Exception as e:
        print(f"❌ Failed to check recent alerts for {ticker}: {e}")
        return False

def get_recent_alerts():
    try:
        recent = (datetime.utcnow() - timedelta(hours=1)).isoformat()
        result = supabase.table("alerts").select("*").gte("timestamp", recent).execute()
        return result.data
    except Exception as e:
        print("❌ Failed to fetch recent alerts:", e)
        return []
