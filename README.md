# New Consumer: Real-Time Total Message Aggregation
The consumer processes real-time JSON messages streamed by the producer and focuses on aggregating the total number of messages for each category. This provides a dynamic insight into which categories receive the most attention over time.
Aggregating total messages reveals the most active or trending categories over time and also it helps seeing the distribution and volume of activity across topics in real-time.

# Insight
Total number of messages per category (e.g. tech, food, gaming)

# Visualization
* Chart Type: Bar Chart - this chart type is good for showing aggregated totals, making easy to compare trends
* Y-axis: Total messages
* X-axis: Categories
  
# Running Producer
python -m producers.project_producer_case

# Running custom consumer
python -m consumers.project_consumer_davidrm

# Git Workflow
git add
git commit -m
git push origin main





