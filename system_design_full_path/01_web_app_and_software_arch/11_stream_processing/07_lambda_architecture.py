# Lambda Architecture
# In this lesson, you will learn about the Lambda architecture of data processing.

# What is lambda architecture?
# Lambda is a distributed data processing architecture that leverages both the batch and the real-time streaming data processing approaches to tackle the latency issues that arise out of the batch processing approach.

# It joins the results from both approaches before presenting them to the end-user. Lambda architecture makes the most of the two approaches.

# system_design_full_path/images/065.png

# Batch processing does take time, considering the massive amounts of data businesses have today. However, the accuracy of the approach is high, and the results are comprehensive.

# On the contrary, real-time streaming data processing provides quick access to insights. In this scenario, the analytics is run over a small portion of data, so the results are not as accurate or comprehensive as the batch approach.

# Layers of the Lambda architecture
# The architecture has typically three layers:

# Batch layer
# Speed layer
# Serving layer
# The batch layer deals with the results acquired via batch processing of the data. The Speed layer gets data from the real-time streaming data processing, and the serving layer combines the results obtained from both the batch and the speed layers.
