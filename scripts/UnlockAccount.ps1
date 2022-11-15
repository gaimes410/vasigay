Import-Module ActiveDirectory

<#

This script takes username as argument
Checks if the user is locked, if yes unlock

#>

$username = $args[0]

function UnlockAccount ()
{
    # This function is unlocking ad account, returns exit code

    try {
        $lockedOut = (Get-ADUser $username -Properties * | Select-Object LockedOut).LockedOut
    }
    catch{
        return 1
    }

    if($lockedOut){
        try{
            Unlock-ADAccount -Identity $username
            return 0
        }
        catch{
            return 1
        }
    }
    else{
        return 0
    }
    $lockedOut = (Get-ADUser $username -Properties * | Select-Object LockedOut).LockedOut
    if ($lockedOut)
    {
        return 1
    }
}

UnlockAccount