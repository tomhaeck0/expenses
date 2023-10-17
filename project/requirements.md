The software

# v0.1.0

- shall accept files containing bank transfers (Argenta csv files)
  - shall offer to the user a file upload field
  - shall validate the input file
  - shall encrypt the uploaded file to protect bank transfer data
  - shall have valid and invalid test files available to test this functionality

- shall write the bank transfer data to a database
  - shall not overwrite existing transfers
  - shall show the bank transfers in Django's admin panel
  - shall show the bank transfers in a Django view
  - shall have a development database, a test database, a production database

- shall show graphically statistics on the number of transfers 
  (e.g. number of transfers for each date)
- shall show a navbar in the browser to switch between views
- shall be a little prettified to make it attractive for the user

- shall be deployed on localhost using Docker

- shall be properly tested (both unit testing and end-to-end testing)


# v0.2.0

- shall have a user management system
  - shall authenticate users
  - shall authorize users to only view bank transfers related to their account