# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC # Notebook Basics  📝
# MAGIC
# MAGIC ## Overview
# MAGIC  
# MAGIC  | Detail Tag | Information |
# MAGIC  |------------|-------------|
# MAGIC  | Created By | [Arodi Hernandez](arhernandez@apexsystems.com)|
# MAGIC  | Updated By | [Luis Camarillo](lcamarillo@apexsystems.com)|
# MAGIC  | History    | This notebook contains material to how to operate a notebook  |
# MAGIC  | Last update  | 5/17/2024 |
# MAGIC  | Content | <ul><li> Run a cell</li></ul>  <ul><li> Write code and text with different formats </li></ul> <ul><li> Upload an image </li></ul>

# COMMAND ----------

# MAGIC %md
# MAGIC # Attach to a cluster
# MAGIC - Connect > Select cluster

# COMMAND ----------

# MAGIC %md
# MAGIC # Notebook Basics
# MAGIC ## 1. Running a cell 
# MAGIC
# MAGIC There are several different ways to run a cell. 
# MAGIC
# MAGIC 1. Use the cell's play button: **Run Cell**, **Run All Above**, or **Run All Below**
# MAGIC 2. **CTRL+ENTER**: Executes selected cell 
# MAGIC 3. **SHIFT+ENTER** Executes selected cell and moves to the next one
# MAGIC 4. Click on the **Run all** button
# MAGIC 5. Use the **Run** menu
# MAGIC
# MAGIC **Note**: Cell by cell execution might mean out of order results, but also allows you to test your code in chunks.

# COMMAND ----------

print("Hello world")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Set the default language.
# MAGIC Databricks supports the following languages:
# MAGIC - Python
# MAGIC - SQL
# MAGIC - Scala
# MAGIC - R
# MAGIC
# MAGIC You can set the default value for the entire notebook above, or change it cell by cell.
# MAGIC

# COMMAND ----------

SELECT * FROM demo.books

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Create and interact with cells
# MAGIC - You can add new code or text cells above or below in your notebook
# MAGIC - Delete cells by clicking on the trash can icon
# MAGIC - Use the keyboard shortcuts available by clicking **H**

# COMMAND ----------

# MAGIC %md
# MAGIC ##4. Magic Commands
# MAGIC - Magic commands are specific to databricks notebooks
# MAGIC - They provide the same outcome regardless of the notebook's language
# MAGIC - A single percent (%) symbol at the start of the cell identifies a magic command
# MAGIC     - You can only have one magic command per cell
# MAGIC     - A magic command must be the first thing in a cell
# MAGIC
# MAGIC ### Language Magics
# MAGIC - You can also select the cell language by typing the language's magic command:
# MAGIC     - **`%python`**
# MAGIC     - **`%sql`**

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Markdown
# MAGIC Text cells can be written using the **Markdown** markup language, rendering formatted. You can also use the **`%md`** to start a Markdown text.
# MAGIC
# MAGIC #  Heading 1
# MAGIC
# MAGIC ## Heading 2
# MAGIC
# MAGIC ### Heading 3
# MAGIC
# MAGIC You can write in normal text, or use:
# MAGIC - **bold**, __bold__
# MAGIC - *italics*, _italics_
# MAGIC - `code`
# MAGIC
# MAGIC You can also create lists, like before, or create ordered lists:
# MAGIC 1. Option 1
# MAGIC 2. Option 2
# MAGIC 3. Option 3
# MAGIC
# MAGIC You can even add images of links: For more information on Markdown options, click [here](https://www.markdownguide.org/basic-syntax/) or review the [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. %run notebooks
# MAGIC - You can run a anotebook from another notebook by using the magic command **`%run`** 
# MAGIC - Notebooks to be run are specified with relative paths
# MAGIC - The referenced notebook executes as if it were part of a current notebook, so temp views or local variables will now be available in the main notebook

# COMMAND ----------

print(secret_variable)

# COMMAND ----------

# MAGIC %run ./0011_Secret_Variable 

# COMMAND ----------

print(secret_variable)

# COMMAND ----------


