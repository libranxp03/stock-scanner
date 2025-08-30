from supabase import create_client
from datetime import datetime, timedelta
import os

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_alert(ticker, tier, score=None):
    try:
        supabase.table("alerts").insert({
            "ticker": ticker,
            "tier": tier,
            "score": score,
            "timestamp": datetime.utcnow().isoformat()
        }).execute()
        print(f"✅ Logged alert for {ticker}")
    except Exception as e:
        print(f"❌ Supabase log failed: {e}")

def get_recent_alerts():
    try:
        recent = (datetime.utcnow() - timedelta(hours=6)).isoformat()
        result = supabase.table("alerts").select("*").gte("timestamp", recent).execute()
        return result.data
    except Exception as e:
        print(f"❌ Supabase fetch failed: {e}")
        return []
