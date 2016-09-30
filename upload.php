<?php

$_FILES['file']['name']=iconv("UTF-8","gb2312", $_FILES['file']['name']);

$savedir="homework/data_structure_2/".$_FILES['file']['name'];
$check='^2015';
$filetype=strrev($_FILES['file']['name']);


$filetype_array=explode(".",$filetype);

$filetype=strrev($filetype_array[0]);

if($filetype=='doc'||$filetype=='docx'||$filetype=='zip'||$filetype=='7z'||$filetype=='rar')
{	
	
 if(@ereg($check,$_FILES['file']['name']))
{
		if(move_uploaded_file($_FILES['file']['tmp_name'],$savedir))
			echo "<script>alert('Upload Success!');window.history.back();</script> ";
		else echo"<script>alert('Maybe the server doesn't work...You can try again or contact me');window.history.back();</script>";
}
 else echo"<script>alert('Wrong Name Forms!The Number should be at the beginning!');window.history.back();</script>";
}
else echo"<script>alert('Wrong Filetype!');window.history.back();</script>";
?>