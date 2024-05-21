# Contents-Tech-Hackathon-DRF

## api/plant/  : Read
>**Plant**
nickname, 
image, 
interest
>
## api/plant/<int:pk>/ : Read
>**Plant**
nickname, image, interest, 
humidity,watering

>**Feedback**
grow_well_count , 
too_many_bugs_count,
leaves_dying_count, 
another_problem_count

>**Species**
good_humidity

## api/plant/<int:pk>/ interest : Update
> **Plant**
interest

## api/plant/<int:pk>/ watering : Update
>**Plant**
watering

## api/plant/<int:pk>/ humidity : Update
>**Plant**
humidity

## api/species : Read
> **Species**
name,
content

## api/feedback :   Create
> **Feedback**
plant,
grow_well,
too_many_bugs,
leaves_dying,
another_problem,

