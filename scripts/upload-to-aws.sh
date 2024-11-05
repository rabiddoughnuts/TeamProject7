
local_upload_path=$(realpath "$1")
remote_upload_path="/home/ubuntu/Classes/TeamProjects/SeniorDesignWebsite/backend/images"

scp -r "$local_upload_path"/* aws:"$remote_upload_path"
echo "Done transferring files to aws"

ssh aws

cd /home/ubuntu/Classes/TeamProjects/SeniorDesignWebsite/backend
npm run dev
