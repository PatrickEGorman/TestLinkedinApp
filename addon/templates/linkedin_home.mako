% if flashed_messages:
    % for message in flashed_messages:
        ${ message }
        <br>
    % endfor
%endif

<form method="post">
    <input type="hidden" name="type" value="login">
    Username:
        <input type="text" name="username" >
    <br>
    Password:
        <input type="password" name="password">
    <br>
    <input type="submit" name="login">

</form>

<form method="post">
    <input type="hidden" name="type" value="create">
    Username:
        <input type="text" name="username" >
    <br>
    Password:
        <input type="password" name="password">
    <br>
    <input type="submit" name="create">

</form>