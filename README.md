# CarRepairBook

CarRepairBook is a web application for storing vehicle maintenance history.
Additional feature is posting repairs and getting offers from mechanics.

## Installation

Use the package manager pip to install requirements.
##### pip install requirements.txt

## Endpoints

### Main page shows all mechanics and their info.
###### /mechanics/

### Responsible for user authentication and login.
###### /vehicle_owner/sign_up/, 
###### /vehicle_owner/sign_in/, 
###### /mechanic/sign_up/, 
###### /mechanic/sign_in/

### Creating vehicle with required arguments.
###### /vehicle/create/

### Full CRUD on repairs. Main functionality.
###### /vehicle/<int:id>/repair/create/
###### /vehicle/repairs/
###### /vehicle/repair/<int:id>/update/
###### /vehicle/repair/<int:id>/delete/
###### /repair/<int:id>/
###### /repairs/

Mechanic user can see all posted repairs and eventually send an offer.
This offer can be accepted. If so repair is no longer seen from other mechanics.
Relation is created between owner and mechanic. 

## Offers
### Full Crud.
###### /offer/repair/<int:id>/create/
###### /offers/
###### /offer/<int:id>/delete/
###### /offer/<int:id>/accept/
