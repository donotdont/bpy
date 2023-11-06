<?php

// $command =  ".\blender\blender -b _swatches.blend " + "Directory\script.py";
//echo system("pwd");
//$command =  "cd /c/Program Files/Blender Foundation/Blender 3.6/ && ./blender -b -python /c/xampp/htdocs/bpy/o.blend -python /c/xampp/htdocs/bpy/script.py";
$command =  "py script.py";

$result = system($command);
//$result = shell_exec($command);

var_dump($result);