
if [ "$#" -ne 1 ]; then
    echo "Error: I need to know the directory to upload"  
    usage
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Not a valid directory"
    usage
    exit 1
fi


local_upload_path=$(realpath "$1")
remote_upload_path="/home/ubuntu/Classes/TeamProjects/SeniorDesignWebsite/backend/images"

sftp aws
local_upload_path/* remote_upload_path
echo "Done transfering files to aws"
