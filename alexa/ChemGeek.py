'use strict';
var Alexa = require('alexa-sdk');

var APP_ID = undefined //OPTIONAL: replace with "amzn1.echo-sdk-ams.app.[your-unique-value-here]";
var SKILL_NAME = 'Chemistry Facts';

/**
 * Array containing chemistry facts.
 */
var FACTS = [
    "The only elements that are liquid at room temperature are bromine and mercury.",
    "Unlike many substances, water expands as it freezes. An ice cube takes up about 9% more volume than the water used to make it.",
    "If you pour a handful of salt into a full glass of water, the water level will actually go down rather than overflowing the glass",
    "A pure element can take many forms. For example, diamond and graphite both are forms of pure carbon.",
    "The only letter that doesn't appear on the periodic table is J.",
    "Lightning strikes produce O 3, which is ozone, and strengthen the ozone layer of the atmosphere.",
    "The only two non-silvery meterals are gold and copper.",
    "THe rarest naturally-occuring element in the earth's crust may be astatine. The entire crust appears to contain about 28 grams of the element.",
    "Bee stings are acidic while wasp stings are alkaline.",
    "Glass is actually a liquid, it just flows very, very slowly."
];

exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var handlers = {
    'LaunchRequest': function () {
        this.emit('GetFact');
    },
    'GetNewFactIntent': function () {
        this.emit('GetFact');
    },
    'GetFact': function () {
        // Get a random chemistry fact from the chemistry facts list
        var factIndex = Math.floor(Math.random() * FACTS.length);
        var randomFact = FACTS[factIndex];

        // Create speech output
        var speechOutput = "Here's your fact: " + randomFact;

        this.emit(':tellWithCard', speechOutput, SKILL_NAME, randomFact)
    },
    'AMAZON.HelpIntent': function () {
        var speechOutput = "You can say tell me a chemistry fact, or, you can say exit... What can I help you with?";
        var reprompt = "What can I help you with?";
        this.emit(':ask', speechOutput, reprompt);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', 'Goodbye!');
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', 'Goodbye!');
    }
};