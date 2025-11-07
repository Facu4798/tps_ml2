try:
    from pyspark.sql import SparkSession
except ImportError:
    import os
    os.system("pip install pyspark")
    from pyspark.sql import SparkSession



