global counter, filename

file read function:
     with open multiple file input, valid, invalid (all three files)
       csv output  reader input
       csv output valid writer
       csv output invalid writer  #all files opened now
       for row
             try
                 unpack row
             except
                 write to invalid file L(error) and row(data)

            invalid_data = false
             try # validating name
                 last, first = '':
            except
                 invalid_data += 'N' (means name)

            invalid_email = false #validating email
            try
                regex email# if fails
            except
                inavlid_email += 'E'

            if invalid_data > ''


main function
     try
         call read function
    except
          process any file i/o errors thrown back
finally
display valid & invalid records