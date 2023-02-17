<h1>C - Hello, World</h1>

<h1>Requirements C</h1>
<p>
  <li>Allowed editors: vi, vim, emacs</li>
  <li>All your files will be compiled on Ubuntu 14.04 LTS using gcc 4.8.4</li>
  <li>All your files should end with a new line</li>
  <li>A README.md file at the root of the alx-systems_enginnering-devops repo, containing a description of the repository</li>
  <li>A README.md file, at the root of the folder of this project, containing a description of the project</li>
  <li>There should be no errors and no warnings during compilation</li>
  <li>Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl</li>
</p>

<h2>File</h2>
<p>This table contains every scripts in the folder, its function and id</p>

<table>
  <h3>
    <tr>
      <th>Script number</th>
      <th>Script Name</th> 
      <th>Description</th>
    </tr>
  </h3>
  <tr>
    <td>0</td>
    <td>0-preprocessor</td> 
    <td>A script that runs a C file through the preprocessor and save the result into another file. The C file name will be saved in the variable $CFILE; The output should be saved in the file c using gcc $CFILE -E -o c.</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1-compiler</td> 
    <td>A script that compiles a C file but does not link. The C file name will be saved in the variable $CFILE; The output file should be named the same as the C file, but with the extension .o instead of .c;

Example: if the C file is main.c, the output file should be main.o using gcc -c $CFILE.</td>
  </tr>
  
  <tr>
    <td>2</td>
    <td>2-path</td> 
    <td>Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>3-paths</td> 
    <td>Counts the number of the directories in the PATH</td>
  </tr>
   
  <tr>
    <td>4</td>
    <td>4-global_variables</td> 
    <td>Lists environment variables</td>
  </tr>
  
  <tr>
    <td>5</td>
    <td>5-local_variables</td> 
    <td>Lists all local variables and environment variables, and functions</td>
  </tr>
  
  <tr>
    <td>6</td>
    <td>6-create_local_variable	</td> 
    <td>Creates a new local variable named BEST with the value school</td>
  </tr>
  
  <tr>
    <td>7</td>
    <td>7-create_global_variable</td> 
    <td>Creates a new global variable named BEST</td>
  </tr>
  
   <tr>
    <td>8</td>
    <td>8-true_knowledge</td> 
    <td>Prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line</td>
  </tr>
  
   <tr>
      <td>9</td>
      <td>9-divide_and_rule</td> 
      <td>Prints the result of POWER divided by DIVIDE, followed by a new line</td>
  </tr>
  
   <tr>
    <td>10</td>
    <td>10-love_exponent_breath</td> 
    <td>Displays the result of BREATH to the power LOVE</td>
  </tr>
  
   <tr>
    <td>11</td>
    <td>11-binary_to_decimal</td> 
    <td>Converts a number from base 2 to base 10</td>
  </tr>
  
   <tr>
    <td>12</td>
    <td>12-combinations</td> 
    <td>Prints all possible combinations of two letters, except oo</td>
  </tr>
	
   <tr>
    <td>13</td>
    <td>13-print_float</td> 
    <td>Prints a number with two decimal places. The number is stored in the environment variable NUM</td>
  </tr>
   
   
   
</table>
