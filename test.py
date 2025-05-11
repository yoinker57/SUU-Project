import pxapi

# Create a Pixie client.
px_client = pxapi.Client(
    token='token',
    server_url='work.getcosmic.ai'
)
# Connect to cluster.
conn = px_client.connect_to_cluster('cluster id')

PXL_SCRIPT = """
import px
df = px.DataFrame('http_events')[['resp_status','req_path']]
df = df.head(10)
px.display(df, 'http_table')
"""

script = conn.prepare_script(PXL_SCRIPT)
# Print the table output.
for row in script.results("http_table"):
    print(row["resp_status"], row["req_path"])