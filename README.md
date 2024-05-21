# Contents-Tech-Hackathon-DRF

api/plant/  : Read

<aside>
💡 **Plant**
nickname, 
image, 
interest
</aside>

api/plant/<int:pk>/ : Read
<aside>
💡 **Plant**
nickname, image, interest, 
humidity,watering

****
**Feedback**
grow_well_count , 
too_many_bugs_count,
leaves_dying_count, 
another_problem_count

****
**Species**
good_humidity

</aside>

api/plant/<int:pk>/ interest : Update

<aside>
💡 **Plant**
interest

</aside>

api/plant/<int:pk>/ watering : Update

<aside>
💡 **Plant**
watering

</aside>

api/plant/<int:pk>/ humidity : Update

<aside>
💡 **Plant**
humidity

</aside>

api/species : Read

<aside>
💡 **Species**
name
content

</aside>

api/feedback :   Create

<aside>
💡 Feedback
plant
grow_well
too_many_bugs
leaves_dying
another_problem

</aside>
