from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# Load the data stored in LIBSVM format as a DataFrame.
data = spark.read.format("libsvm").load("/FileStore/tables/colon_cancer_01.txt")

# Index labels, adding metadata to the label column.
# Fit on whole dataset to include all labels in index.
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)

# Automatically identify categorical features, and index them.
# We specify maxCategories so features with > 4 distinct values are treated as continuous.
featureIndexer =VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)

# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])

# Train a DecisionTree model.
dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures")

# Chain indexers and tree in a Pipeline
pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])

# Select (prediction, true label) and compute test error
evaluator1 = MulticlassClassificationEvaluator(
    labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")

paramGrid = ParamGridBuilder() \
    .addGrid(dt.maxBins, [2, 5, 10, 20]) \
    #.addGrid(dt.impurity, ['gini','entropy']) \
    .build()

crossval = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid,
                          evaluator=evaluator1,
                          numFolds=3)  # use 3+ folds in practice


# Train model.  This also runs the indexers.
cvModel = crossval.fit(trainingData)

# Make predictions.
predictions = cvModel.transform(testData)

# Select example rows to display.
predictions.select("prediction", "indexedLabel", "features").show(5)

    
accuracy = evaluator1.evaluate(predictions)
print("Test Error = %g " % (1.0 - accuracy))

