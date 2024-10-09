import altair as alt
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

def read_parking_tickets(file_path):
    start_time = time.time()
    df = pd.read_csv(file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert len(df) == 287458, "The number of rows is not as expected."
    print(f"Time taken to read the file: {elapsed_time:.2f} seconds")
    return df

file_path = 'minilessons\minilesson_2\data\parking_tickets_one_percent.csv'
df = read_parking_tickets(file_path)

ticket_freq = df['vehicle_make'].value_counts()

paid_tickets = df[df['ticket_queue'] == 'Paid'].groupby('vehicle_make').size()
paid_fraction = dict(paid_tickets / ticket_freq)

paid_fraction = paid_fraction.sort_values(ascending=False).reset_index()
print(paid_fraction.head())
paid_fraction.columns = ['vehicle_make', 'fraction_paid'] 

alt.Chart(paid_fraction.head(20)).mark_bar().encode(
    alt.X('vehicle_make:N', title = "Vehicle Make", sort = '-y'), 
    alt.Y('fraction_paid:Q', title = "Fraction Paid") 
).properties(
    title='Fraction of Tickets Paid by Vehicle Make',
    width=500,
    height=300
)

df['issue_date'] = pd.to_datetime(df['issue_date'])

df['date'] = df['issue_date'].dt.strftime('%Y-%m')
tickets_by_date = df.groupby('date').size().reset_index()
tickets_by_date.columns = ['Date', 'Number of Tickets per Month']

alt.Chart(tickets_by_date).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='Date:T',
    y='Number of Tickets per Month:Q'
)