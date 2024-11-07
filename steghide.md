## Step 1 Embed:

steghide embed -cf `~/path/to/image.jpg` -ef `~/data/to/embed`

Enter passphrase:

Re-Enter passphrase:

embedding `"~/data/to/embed"` in `"~/path/to/image.jpg"`... done

## Step 2 Extract:
steghide extract -sf `~/path/to/image.jpg`

Enter passphrase:

wrote extracted data to "embed".

## Notes
 - Extracted data will have the same file name but will output into the home directory
 - There is no built in option to change output location
 - Steghide does not support PNG

`-z, --compress`             --compress data before embedding (default)
 
`-z <l>`                   --using level <l> (1 best speed...9 best compression)

 - The first argument must be one of the following:
   - embed, --embed             embed data
   - extract, --extract         extract data
   - info, --info               display information about a cover- or stego-file
   - info `<filename>`          --display information about `<filename>`
   - encinfo, --encinfo         display a list of supported encryption algorithms
   - version, --version         display version information
   - license, --license         display steghide's license
   - help, --help               display this usage information
