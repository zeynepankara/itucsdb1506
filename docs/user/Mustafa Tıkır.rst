##################################
Parts Implemented by Mustafa TIKIR
##################################
   When the user click to records bar in the main page, records of the swimmers is going to appear.

   .. figure:: TIKIR/MainPage.png
      :scale: 50 %
      :alt: Main

      *This is the main page*

   Click to the records bar

   .. figure:: TIKIR/RecordsPage.png
      :scale: 50 %
      :alt: Records

      *This is the records page*

   Records page has been appeared.

   In Records page there are 3 tables about swimmer records, and all these tables have 4 functions for each one.

   These tables are:

1. Record List
2. High Scores List for Records
3. Lowest Scores List for Records

   Functions for each one have same name and functionality, and their names are:

1. Add
2. Delete
3. Update
4. Search


Functions are going to be explained in the tables

1. Record List
==============
   This table lists the records of the swimmers. It consists of the swimmers of other 2 tables and additional swimmers.

   This is the main table for this project. If user wants to add an swimmer record to other tables or update some data,
   its score have to be in this table.

   In this table there are 2 attributes for user to enter, and one secret attribute that is enabled for default
    for ordering the records.

   So, 2 attributes are always shown at the screen.

   These attributes are:

   1. Name of the swimmer  : it is an string attribute
   2. Score                : it is an integer attribute
   3. ID of swimmer        : it is an also integer attribute, but it is enabled by default

   Let me explain the functions

1.1 Add function
----------------
   The first function that I am going to explain is add function for Records list.

   In the Records Page, at the top of the page, there is an button, and it is add button.

   If the user wants to add some record to the table, he or she should click to button first.

   .. figure:: TIKIR/AddFuctionRecordList1.png
      :scale: 50 %
      :alt: Add Function for Record List

      *Add button is shown at the top of the page*

   When add button is clicked, the address of wab page is going to be changed and an simple form page will appear.

   .. figure:: TIKIR/AddFuctionRecordList2.png
      :scale: 50 %
      :alt: Add Function form for Record List

      *Add form*

   At this page, the user should write an string for the name and integer for the record.

   After user write the data, it is enough to click to save button being at the button of the page.

   And as it is shown below, it is added to Records list.

   .. figure:: TIKIR/AddFuctionRecordList3.png
      :scale: 50 %
      :alt: Data is added for Record List

      *The new appearance of Record list with new data*

1.2 Delete function
-------------------
   It is really easy to delete an row(tuple) from the table.

   As shown below, there is an empty button for each row of table, and at the bottom there is delete button.

   .. figure:: TIKIR/DeleteFuctionRecordList1.png
      :scale: 50 %
      :alt: Delete function for Record List

      *This screen cast shows how the delete function works*

   When one of the empty button is clicked and the delete is pressed, then that row of the table is going to be deleted.

   As it is shown below, it is deleted from the Records list.

   .. figure:: TIKIR/DeleteFuctionRecordList2.png
      :scale: 50 %
      :alt: After delete operation is done for Record List

      *The new appearance of Record list after the delete operation is implemented.*

   **Important Note**

   As I mentioned before, the value is going to be deleted do not have to be in the other tables.

   What if it is in the other tables, there is going to appear an error message.

   This error message is shown below

   .. figure:: TIKIR/DeleteFuctionRecordList3.png
      :scale: 50 %
      :alt: After an invalid tuple try to delete

      *Error message after invalid tuple tried to be deleted*

1.3 Update function
-------------------

   Update function updates the data in the Records list.

   For update an row of the table, the user should first select the update button which is at the bottom.

   .. figure:: TIKIR/UpdateFuctionRecordList1.png
      :scale: 50 %
      :alt: Update operation for Record List

      *User needs to click to update button first*

   After user clicked to update button, an new web page appears. That web page shows all the attributes and tuples of the table.

   And, all rows have an button their left hand side for selecting the tuple which is going to be updated.

   The user should select one of these and should fulfilled the form with true types of characters.

   And then, user should click the update.

   .. figure:: TIKIR/UpdateFuctionRecordList2.png
      :scale: 50 %
      :alt: Update form for Record List

      *This screen cast shows how the update form seems and works*

   After the all necessary things is done in update form. The new appearance of Record page with updated data appears.

   .. figure:: TIKIR/UpdateFuctionRecordList3.png
      :scale: 50 %
      :alt: After update operation is done for Record List

      *Record list with updated data*

   **Important Note**

   What if the record with existing in the other tables want to be updated?

   The answer is the name of that tuple can be updated, but score of that tuple cannot be updated. So, it stays same in
   case it is tried to be changed.

1.4 Search function
-------------------

   The another and last function for Records table is search function.

   It is easy to implement. Click to search function which is below of the table and shown below figure

   .. figure:: TIKIR/SearchFuctionRecordList1.png
      :scale: 50 %
      :alt: Search operation for Record List

      *Click to search*

   If user clicks to search function, the web site turns an new page and that page request an name for searching

   .. figure:: TIKIR/SearchFuctionRecordList2.png
      :scale: 50 %
      :alt: Search form for Record List

      *Type the full name of swimmer for searching*

   The user should write the full name of the swimmer for searching.

   After user write it, the page shown below appears

   .. figure:: TIKIR/SearchFuctionRecordList3.png
      :scale: 50 %
      :alt: After Search operation for Record List

      *The page after search operation correctly done*

   If invalid name is entered, the page is going to show no value.

2. High Scores List for Records
===============================
   This table lists only the records of swimmer who has high score.

   Actually there is no restriction about adding or deleting any records with high score or low score.

   However, because of logical integrity, high scores are expected to enter from the user.

   This table and other 2 tables are quite similar to each other. So, these tables are not going to be explained very deeply.

   Also,  in this table there are 2 attributes for user to enter, and one secret attribute that is enabled for default
    for ordering the records.

   So, 2 attributes are always shown at the screen.

   These attributes are:

   1. Name of the swimmer  : it is an string attribute
   2. Highest Score         : it is an integer attribute
   3. ID of swimmer        : it is an also integer attribute, but it is enabled by default


   This table is shown like this:

   .. figure:: TIKIR/HighRecords.png
      :scale: 50 %
      :alt: High Records

      *Records with high scores are shown*


   Let me explain the functions briefly

2.1 Add function
----------------

   Add function of High Score List for Records is nearly similar to Records list.

   **Important Note**
   At the add operation, user should enter an score that already exist in Records list.


   In the Records Page, at the mid of the page, there is an button, and it is add High Scores button for High Scores.

   If the user wants to add some record to the table, he or she should click to button first.

   .. figure:: TIKIR/AddFuctionHighRecordList1.png
      :scale: 50 %
      :alt: Add Function for High Score list for records

      *Add button is shown at the mid of the page*

   When add button is clicked, the address of web page is going to be changed and an simple form page will appear.

   .. figure:: TIKIR/AddFuctionHighRecordList2.png
      :scale: 50 %
      :alt: Add Function form for High scores list for records

      *Add form*

   At this page, the user should write an string for the name and integer for the record.

   After user write the data, it is enough to click to save button being at the bottom of the page.

   And as it is shown below, it is added to High scores list for records.

   .. figure:: TIKIR/AddFuctionHighRecordList3.png
      :scale: 50 %
      :alt: Data is added for Record List

      *The new appearance of High scores list for records with new data*

   If entered swimmers record does not exist in the Records list, then there is going to appear an error message.

   .. figure:: TIKIR/AddFuctionHighRecordList4.png
      :scale: 50 %
      :alt: Error

      *Error message after added invalid swimmer record*

2.2 Delete fuction
------------------

   Deletion operation for High Scores is similar with the Records table's deletion.

   As shown below, there is an empty button for each row of table, and at the bottom there is delete button.

   .. figure:: TIKIR/DeleteFuctionHighRecordList1.png
      :scale: 50 %
      :alt: Delete function for High scores list for records

      *This screen cast shows how the delete function works for High Scores table*

   When one of the empty button is clicked and the delete is pressed, then that row of the table is going to be deleted.

   As it is shown below, it is deleted from the Records list.

   .. figure:: TIKIR/DeleteFuctionHighRecordList2.png
      :scale: 50 %
      :alt: After delete operation is done for High Scores list for record List

      *The new appearance of High scores list for records, after the delete operation is implemented.*


2.3 Update function
-------------------

   Update function updates the data in the High scores list for Records.

   For update an row of the table, the user should first select the update button which is at the mid of the page.

   .. figure:: TIKIR/UpdateFuctionHighRecordList1.png
      :scale: 50 %
      :alt: Update operation for High scores list for Records

      *User needs to click to update button first*

   After user clicked to update button, an new web page appears. That web page shows all the attributes and tuples of the table.

   And, all rows have an button their left hand side for selecting the tuple which is going to be updated.

   The user should select one of these and should fulfilled the form with true types of characters.

   And then, user should click the update.

   .. figure:: TIKIR/UpdateFuctionHighRecordList2.png
      :scale: 50 %
      :alt: Update form for High scores list for Records

      *This screen cast shows how the update form seems and works*

   After the all necessary things is done in update form. The new appeance of Record page with updated data appears.

   .. figure:: TIKIR/UpdateFuctionHighRecordList3.png
      :scale: 50 %
      :alt: After update operation is done for High scores list for Records

      *High scores list for Records with updated data*

   **Important Note**

   If updated score of that record does not exist in the Records list, the program is going to give an error.

   So, the user have to update the score that is existing in the Record list.

2.4 Search function
-------------------

   The another and last function for High scores list for Records table is search function.

   It is easy to implement. Click to search function which is below of the table and shown below figure

   .. figure:: TIKIR/SearchFuctionHighRecordList1.png
      :scale: 50 %
      :alt: Search operation for High scores list for Records

      *Click to search*

   If user clicks to search function, the web site turns an new page and that page request an name for searching

   .. figure:: TIKIR/SearchFuctionHighRecordList2.png
      :scale: 50 %
      :alt: Search form for High scores list for Records

      *Type the full name of swimmer for searching*

   The user should write the full name of the swimmer for searching.

   After user write it, the page shown below appears

   .. figure:: TIKIR/SearchFuctionHighRecordList3.png
      :scale: 50 %
      :alt: After Search operation for High scores list for Records

      *The page after search operation correctly done*

   If invalid name is entered, the page is going to show no value.

3. Lowest Scores List for Records
=================================

   This table lists only the records of swimmer who has low score. This table's functions and table's itself quite similar to High
   scores table.


3.1 Add function
----------------

   Add function of Lowest Scores List for Records is nearly similar to Records list and quite similar to High Scores table

   **Important Note**
   At the add operation, user should enter an score that already exist in Records list.

   In the Records Page, at the bottom of the page, there is an button, and it is add Lowest  Scores button for High Scores.

   If the user wants to add some record to the table, he or she should click to button first.

   .. figure:: TIKIR/AddFuctionLowRecordList1.png
      :scale: 50 %
      :alt: Add Function for Low Scores list for records

      *Add button is shown at the nearly bottom of the page*

   When add button is clicked, the address of web page is going to be changed and an simple form page will appear.

   .. figure:: TIKIR/AddFuctionLowRecordList2.png
      :scale: 50 %
      :alt: Add Function form for Lowest scores list for records

      *Add form*

   At this page, the user should write an string for the name and integer for the record.

   After user write the data, it is enough to click to save button being at the bottom of the page.

   And as it is shown below, it is added to Lowest scores list for records.

   .. figure:: TIKIR/AddFuctionLowRecordList3.png
      :scale: 50 %
      :alt: Data is added for Record List

      *The new appearance of Lowest scores list for records with new data*

   If entered swimmers record does not exist in the Records list, then there is going to appear an error message.

   .. figure:: TIKIR/AddFuctionLowRecordList4.png
      :scale: 50 %
      :alt: Error

      *Error message after added invalid swimmer record*


3.2 Delete function
-------------------

   Deletion operation for Lowest Scores is similar with the Records table's deletion, and quite similar with the High Score's one.

   As shown below, there is an empty button for each row of table, and at the buttom there is delete button.

   .. figure:: TIKIR/DeleteFuctionLowRecordList1.png
      :scale: 50 %
      :alt: Delete function for Low scores list for records

      *This screen cast shows how the delete function works for Low Scores table*

   When one of the empty button is clicked and the delete is pressed, then that row of the table is going to be deleted.

   As it is shown below, it is deleted from the Records list.

   .. figure:: TIKIR/DeleteFuctionLowRecordList2.png
      :scale: 50 %
      :alt: After delete operation is done for Low Scores list for record List

      *The new appearance of Low scores list for records, after the delete operation is implemented.*


3.3 Update function
-------------------

   Update function updates the data in the High scores list for Records.

   For update an row of the table, the user should first select the update button which is at the bottom of the page.

   .. figure:: TIKIR/UpdateFuctionLowRecordList1.png
      :scale: 50 %
      :alt: Update operation for Lowest scores list for Records

      *User needs to click to update button first*

   After user clicked to update button, an new web page appears. That web page shows all the attributes and tuples of the table.

   And, all rows have an button their left hand side for selecting the tuple which is going to be updated.

   The user should select one of these and should fulfilled the form with true types of characters.

   And then, user should click the update.

   .. figure:: TIKIR/UpdateFuctionLowRecordList2.png
      :scale: 50 %
      :alt: Update form for Lowest records list for records

      *This screen cast shows how the update form seems and works*

   After the all necessary things is done in update form. The new appearance of Record page with updated data appears.

   .. figure:: TIKIR/UpdateFuctionLowRecordList3.png
      :scale: 50 %
      :alt: After update operation is done for Lowest records list for records

      *High scores list for Records with updated data*

   **Important Note**

   If updated score of that record does not exist in the Records list, the program is going to give an error.

   So, the user have to update the score that is existing in the Record list.

3.4 Search function
-------------------

   The another and last function for low scores list for Records table is search function.

   It is easy to implement. Click to search function which is below of the table and shown below figure

   .. figure:: TIKIR/SearchFuctionLowRecordList1.png
      :scale: 50 %
      :alt: Search operation for Low scores list for Records

      *Click to search*

   If user clicks to search function, the web site turns an new page and that page request an name for searching

   .. figure:: TIKIR/SearchFuctionLowRecordList2.png
      :scale: 50 %
      :alt: Search form for Lowest scores list for Records

      *Type the full name of swimmer for searching*

   The user should write the full name of the swimmer for searching.

   After user write it, the page shown below appears

   .. figure:: TIKIR/SearchFuctionLowRecordList3.png
      :scale: 50 %
      :alt: After Search operation for Lowest scores list for Records

      *The page after search operation correctly done*

   If invalid name is entered, the page is going to show no value.

