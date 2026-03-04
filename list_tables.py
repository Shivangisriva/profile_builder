from supabase_client import supabase
import json

def list_available_tables():
    """
    Try to query common table names and see which ones exist.
    This helps identify the correct table structure in Supabase.
    """
    print("🔍 Checking for available tables in Supabase...")
    print("="*60)
    
    # Common table name variations to try
    possible_tables = [
        "users",
        "Users", 
        "User",
        "user",
        "profiles",
        "Profiles",
        "Profile",
        "profile"
    ]
    
    found_tables = []
    
    for table_name in possible_tables:
        try:
            # Try to fetch just one record to see if table exists
            response = supabase.table(table_name).select("*").limit(1).execute()
            found_tables.append(table_name)
            print(f"✅ Found table: '{table_name}'")
            if response.data:
                print(f"   Sample columns: {list(response.data[0].keys())}")
        except Exception as e:
            print(f"❌ Table '{table_name}' not found")
    
    print("="*60)
    if found_tables:
        print(f"\n✅ Found {len(found_tables)} accessible table(s): {', '.join(found_tables)}")
    else:
        print("\n⚠️  No tables found with common names.")
        print("   Please check your Supabase dashboard for the correct table names.")
    
    return found_tables

if __name__ == "__main__":
    list_available_tables()
