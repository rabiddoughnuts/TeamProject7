if [ "$#" -ne 2 ]; then
    echo "Error: I need to know the directory to upload"  
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Not a valid directory"
    exit 1
fi

local_upload_path=$(realpath "$1")
remote_upload_path="/home/ubuntu/Classes/TeamProjects/SeniorDesignWebsite/backend/images"

scp -r "$local_upload_path"/* aws:"$remote_upload_path"
echo "Done transferring files to aws"

ssh aws

cd /home/ubuntu/Classes/TeamProjects/SeniorDesignWebsite/backend
npm run dev
