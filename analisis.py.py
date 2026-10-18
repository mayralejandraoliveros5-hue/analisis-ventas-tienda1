

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AnalisisVentas").getOrCreate()

datos = spark.read.csv("ventas.csv", header=True, inferSchema=True)

print("DATOS DE LAS VENTAS")
datos.show()

print("INGRESOS POR PRODUCTO")
datos.groupBy("producto").sum("total_venta").show()

print("CANTIDAD VENDIDA POR PRODUCTO")
datos.groupBy("producto").sum("cantidad").show()

print("INGRESOS POR FECHA")
datos.groupBy("fecha").sum("total_venta").show()

spark.stop()

