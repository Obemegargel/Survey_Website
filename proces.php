<?php
    $keys = array('lastapartmentoption', 'oneoption', 'twooption', 'threeoption', 'fouroption', 'fiveeoption', 
    'apartmentoption', 'housingoption', 'falloption', 'springoption', 'summeroption', 'winteroption', 
    'yearinput', 'costinput');
    $csv_line = array();
    foreach($keys as $key){
        array_push($csv_line,'' . $_GET[$key]);
    }
    $fname = 'file_to_write_to.csv';
    $csv_line = implode(',',$csv_line);
    if(!file_exists($fname)){$csv_line = "\r\n" . $csv_line;}
    $fcon = fopen($fname,'a');
    $fcontent = $csv_line;
    fwrite($fcon,$csv_line);
    fclose($fcon);

    //echo file_get_contents($fname);//this is extra may remove it later
?>