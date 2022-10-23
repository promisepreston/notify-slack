# README.md

**Note**: This is still a work in progress. Contributions are welcome.

This is a Lambda function that receives messages from an SNS queue and sends it to a specified Slack Channel. It includes logic to transform your SNS topic's notification messages for the type of webhook endpoint that you're using and is compatible with the **Python 3.9** runtime.

Slack Incoming Webhooks expect a JSON request with a message string corresponding to a "text" key. They also support message customization, such as adding a user name and icon, or overriding the webhook's default channel. For more information, see [Sending messages using incoming webhooks](https://aws.amazon.com/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/#:~:text=Sending%20messages%20using%20incoming%20webhooks) on the Slack website.

This project contains:

* `index.py` file - The file containing the lambda function
* `.circleci` folder - A folder that contains the `config.yml` for deployment using [Circle CI](https://app.circleci.com/) to Amazon Web Services (AWS) Lambda Function if you want to.
* `README.md` file - The file contains the lambda function setup guide

## Create Incoming webhooks for Slack

Incoming webhooks are a simple way to share information from external sources with your workspace:

1. [Create a new Slack app](https://api.slack.com/apps/new) in the workspace where you want to post messages.
2. From the Features page, toggle **Activate Incoming Webhooks** on.
3. Click **Add New Webhook to Workspace**.
4. Pick a channel that the app will post to, then click **Authorize**.
5. Use your [Incoming Webhook URL](https://api.slack.com/incoming-webhooks#posting_with_webhooks) to post a message to Slack.

**Note**: Check out our [Slack API documentation](https://api.slack.com/incoming-webhooks#) for more details about using incoming webhooks.

## Create an SNS topic

If you haven't done so already, [create an SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html) with a unique name.

## Create a Lambda function

For instructions to create a Lambda function, see [Getting started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html). For more information, see [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/en_us/lambda/latest/dg/with-sns.html).

Your Lambda function will contain the `index.py` file which is the code that includes logic to transform your SNS topic's notification messages for the type of Slack webhook endpoint.

## Environment Variables

Set the following environment variables for the Lambda function:

* SLACK_WEBHOOK_URL - The Slack Webhook URL. An example is `https://hooks.slack.com/services/T020CSDKTR5/B0472HJAAC8/DpkDFDGRg4q4yt40VFHbwKz`
* SLACK_CHANNEL - The Slack Channel. An example is `#aws-notifications`
* SLACK_ICON_EMOJI - The Slack Icon Emoji. An example is `:aws:`
* SLACK_USERNAME - Your preferred Slack Username. An example is `aws-cloudwatch`

## Test the Lambda function

1. On the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console, choose your function.
2. Choose the **Test** dropdown list. Then, choose **Configure test event**.
3. In the **Configure test event** dialog box, choose **Create new event**.
4. For **Event template**, choose **SNS Topic Notification**.
5. For **Event name**, enter a name for the test event.
6. Choose **Save**.
7. After it's saved, choose **Test**. Then, review the **Execution result**.

If the test invocation succeeds with a 200 status code, then the Amazon SNS notification message is accepted by your webhook, which delivers it to the corresponding channel. If the invocation fails with a 4xx status code, then check the webhook URL to verify that the key-value pair is correct and accepted by your destination webhook.

For more information about testing functions in the Lambda console, see [Invoke the Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#get-started-invoke-manually).

## Add an SNS topic trigger to your Lambda function

After sending an SNS message to your webhook as a test in the Lambda console, subscribe your function to your SNS topic. To configure this from the Lambda console, add an SNS topic trigger:

1. On the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console, choose your function.
2. Under **Function overview**, choose **Add trigger**. For more information, see [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html).
3. Under **Trigger configuration**, choose **Select a trigger**. Then, choose **SNS**.
4. For **SNS topic**, choose the SNS topic that you created earlier.
5. Choose **Add**.

For more information, see [Configuring functions (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-common-summary).

With your function subscribed to your SNS topic, [messages published to the topic](https://docs.aws.amazon.com/sns/latest/dg/sns-publishing.html) are forwarded to the function, and then to your webhook.

**Note**: For information on how to get Amazon SNS notifications through other AWS services, see [Monitoring AWS Services using AWS Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/related-services.html).

## Reference

1. [How do I use webhooks to publish Amazon SNS messages to Amazon Chime, Slack, or Microsoft Teams?](https://aws.amazon.com/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/)
