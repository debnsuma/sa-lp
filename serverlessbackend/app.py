from chalice import Chalice
import boto3
from hashlib import blake2b



app = Chalice(app_name='serverlessbackend')
BUCKET_NAME = "liveproject2021"
@app.route('/presignedurl', methods=['GET'], cors=cors_config)
def  presigned_url(email):
    mail = app.current_request.query_params.get('mail')

    print("query_param mail: " + mail)

    if len(mail) == 0:
        raise NotFoundError("mail is empty " + mail)

    h = blake2b(digest_size=10)
    h.update(b'Replacing SHA1 with the more secure function')
    hexmail = h.hexdigest()
    print("hex mail: " + hexmail)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(Bucket=BUCKET_NAME,
                                                     Key=hexmail + '.mp4',
                                                     Fields={"acl": "public-read"},
                                                     Conditions=[{
                                                         'acl': 'public-read'
                                                     }],
                                                     ExpiresIn=3600)
    except ClientError as e:
        logging.error(e)
        raise BadRequestError("Internal Error generating presigned post ")
    return response
