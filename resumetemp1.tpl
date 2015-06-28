<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;
}
</style>
</head>

Above Average-
<table>
<tr>
<th>Enrollment no.</th>
<th>First Name</th>
<th>Middle Name</th>
<th>Last Name</th>
<th>Objective</th>
<th>Address</th>
<th>city</th>
<th>state</th>
<th>pin</th>
<th>email_id</th>
<th>phno</th>
<th>college_name</th>
<th>affiliated_to</th>
<th>current_cgpa</th>
<th>twelth_percent</th>
<th>tenth_percent</th>
<th>tech_skills</th>
<th>it_organization</th>
<th>it_description</th>
<th>it_duration</th>
<th>it_role</th>
<th>mi_organization</th>
<th>mi_description</th>
<th>mi_duration</th>
<th>mi_role</th>
<th>ma_organization</th>
<th>ma_description</th>
<th>ma_duration</th>
<th>ma_role</th>
<th>ec_activities</th>
<th>achievements</th>
<th>strength</th>
<th>weakness</th>
<th>hobbies</th>
<th>dob</th>
<th>gender</th>
<th>nationality</th>
<th>marital_status</th>
<th>lang_known</th>
<th>mother_tongue</th>
<th>fathers_name</th>
<th>hod_name</th>
<th>date</th>
<th>year</th>

</tr>
%for row in rows1:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>

Below Average-
<table>
<tr>
<th>Enrollment no.</th>
<th>First Name</th>
<th>Middle Name</th>
<th>Last Name</th>
<th>Objective</th>
<th>Address</th>
<th>city</th>
<th>state</th>
<th>pin</th>
<th>email_id</th>
<th>phno</th>
<th>college_name</th>
<th>affiliated_to</th>
<th>current_cgpa</th>
<th>twelth_percent</th>
<th>tenth_percent</th>
<th>tech_skills</th>
<th>it_organization</th>
<th>it_description</th>
<th>it_duration</th>
<th>it_role</th>
<th>mi_organization</th>
<th>mi_description</th>
<th>mi_duration</th>
<th>mi_role</th>
<th>ma_organization</th>
<th>ma_description</th>
<th>ma_duration</th>
<th>ma_role</th>
<th>ec_activities</th>
<th>achievements</th>
<th>strength</th>
<th>weakness</th>
<th>hobbies</th>
<th>dob</th>
<th>gender</th>
<th>nationality</th>
<th>marital_status</th>
<th>lang_known</th>
<th>mother_tongue</th>
<th>fathers_name</th>
<th>hod_name</th>
<th>date</th>
<th>year</th>
</tr>
%for row in rows2:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>

