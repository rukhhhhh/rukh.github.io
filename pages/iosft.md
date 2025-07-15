# iOS Financial Tracker

I came up with this Financial Tracker as I got tired of manually logging my daily expenses into a sheet. I thought that the best quality of life improvement would be to be able to run a logging script using the iPhone Shortcuts app. The input will be the Action button in iPhone 15 & above. This project is not documented in full; the full capability consists of it exporting each sheet at the end of each month to an annual expense tracker.


## Table of Contents

* [iOS Shorcuts](#ios-shortcuts)

### iOS Shortcuts

Using the shortcuts app and a little bit of research, I came up with a script that runs when activated with the action button. 

```json
{
   "WFWorkflowMinimumClientVersionString": "3010",
   "WFWorkflowMinimumClientVersion": 3010,
   "WFWorkflowIcon": {
      "WFWorkflowIconStartColor": 2846468607,
      "WFWorkflowIconGlyphNumber": 59395
   },
   "WFWorkflowClientVersion": "3607.0.2",
   "WFWorkflowOutputContentItemClasses": [],
   "WFWorkflowHasOutputFallback": false,
   "WFWorkflowActions": [
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "UUID": "930C7864-ADA4-428D-AEB1-99BC84552897",
            "WFTextActionText": "Sharukh Khan"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuPrompt": "Expense or Income: ",
            "WFControlFlowMode": 0,
            "WFMenuItems": [
               "Expense",
               "Income"
            ],
            "GroupingIdentifier": "B3D6ECA2-942E-4296-A732-8CCB473A2ACE"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Expense",
            "GroupingIdentifier": "B3D6ECA2-942E-4296-A732-8CCB473A2ACE",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "UUID": "7195C7A8-AF06-422F-BC72-34DE64B8884F",
            "WFTextActionText": "expense"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "7195C7A8-AF06-422F-BC72-34DE64B8884F",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "expenditure"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuPrompt": "Category: ",
            "WFControlFlowMode": 0,
            "WFMenuItems": [
               "Transportation",
               "Food",
               "Entertainment",
               "Bills",
               "Gifts",
               "Personal",
               "Health",
               "Travel",
               "Miscellaneous "
            ],
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Transportation",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Transportation",
            "UUID": "F46F0D5C-8F4A-4EC7-9DA0-6C3F8A2D7375"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "F46F0D5C-8F4A-4EC7-9DA0-6C3F8A2D7375",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Food",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Food",
            "UUID": "28522DC4-4E66-4173-AB4D-BA0D3657C7F1"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "28522DC4-4E66-4173-AB4D-BA0D3657C7F1",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Entertainment",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Entertainment",
            "UUID": "FE283F1D-90DB-468A-BDCF-8ECFCBBFCEF3"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "FE283F1D-90DB-468A-BDCF-8ECFCBBFCEF3",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Bills",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Bills",
            "UUID": "D886CD55-9BDD-4BCE-8734-95109B2C9406"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "D886CD55-9BDD-4BCE-8734-95109B2C9406",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Gifts",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Gifts",
            "UUID": "D73E9A75-797F-4358-9065-0EE3D8CA24CB"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "D73E9A75-797F-4358-9065-0EE3D8CA24CB",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Personal",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Personal",
            "UUID": "9D4CA24E-EF75-44A0-B4E5-5225801AD264"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "9D4CA24E-EF75-44A0-B4E5-5225801AD264",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Health",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Health",
            "UUID": "1180052C-545B-48B2-AF6E-E0F095D8F537"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "1180052C-545B-48B2-AF6E-E0F095D8F537",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Travel",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Travel",
            "UUID": "80170CAE-3F5C-447B-874E-46FF59E8E59A"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "80170CAE-3F5C-447B-874E-46FF59E8E59A",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Miscellaneous ",
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Other",
            "UUID": "D2FF712E-3EC9-40EF-8F5B-3FE3F28CB694"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "D2FF712E-3EC9-40EF-8F5B-3FE3F28CB694",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFControlFlowMode": 2,
            "GroupingIdentifier": "79B0DBA3-A48C-456F-8175-8CE4146D4A91",
            "UUID": "C0407397-34D6-4043-A11E-954B5D95A9D4"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Income",
            "GroupingIdentifier": "B3D6ECA2-942E-4296-A732-8CCB473A2ACE",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "income",
            "UUID": "977E9025-5472-4581-BC77-32953089E7A3"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "977E9025-5472-4581-BC77-32953089E7A3",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "expenditure"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuPrompt": "Select: ",
            "WFControlFlowMode": 0,
            "WFMenuItems": [
               "Savings",
               "Salary",
               "PayNow / Bank Transfer",
               "Deposit",
               "Bonus",
               "Other"
            ],
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Savings",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Savings",
            "UUID": "0EF45AAB-E7C5-493D-A2F9-E241EAC0A9DC"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "0EF45AAB-E7C5-493D-A2F9-E241EAC0A9DC",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Salary",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Salary",
            "UUID": "AAE46077-595B-4B00-BFAB-C139FB958A13"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "AAE46077-595B-4B00-BFAB-C139FB958A13",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "PayNow / Bank Transfer",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "PayNow",
            "UUID": "5D3ACF2F-C634-4F37-8401-721E44260D7F"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "5D3ACF2F-C634-4F37-8401-721E44260D7F",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Deposit",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "UUID": "28056352-8962-4E40-8F92-E429B54D7988"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "28056352-8962-4E40-8F92-E429B54D7988",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Bonus",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Bonus",
            "UUID": "69F5A44E-256D-4059-B3BF-71DE906B3893"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "69F5A44E-256D-4059-B3BF-71DE906B3893",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Other",
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Other",
            "UUID": "ACA6A50F-D295-4CC2-B39D-F23EA2E58B7D"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "ACA6A50F-D295-4CC2-B39D-F23EA2E58B7D",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "category"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "GroupingIdentifier": "4E2F70B0-5D32-4A47-82C3-9565F10214D7",
            "WFControlFlowMode": 2
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFControlFlowMode": 2,
            "GroupingIdentifier": "B3D6ECA2-942E-4296-A732-8CCB473A2ACE",
            "UUID": "ECBFFFB0-CBE9-4F53-A2DE-05C0137045A0"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.ask",
         "WFWorkflowActionParameters": {
            "WFAskActionAllowsNegativeNumbers": false,
            "UUID": "6A3AF0C3-BA22-4F8A-87EE-9E5501371525",
            "WFInputType": "Number",
            "WFAskActionPrompt": "Amount?"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "6A3AF0C3-BA22-4F8A-87EE-9E5501371525",
                  "Type": "ActionOutput",
                  "OutputName": "Ask for Input"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "amount"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Type": "Variable",
               "Variable": {
                  "Value": {
                     "VariableName": "expenditure",
                     "Type": "Variable"
                  },
                  "WFSerializationType": "WFTextTokenAttachment"
               }
            },
            "WFControlFlowMode": 0,
            "WFConditionalActionString": "income",
            "GroupingIdentifier": "A6305465-0182-4EA4-9B67-0C64F466F347",
            "WFCondition": 4
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFConditions": {
               "Value": {
                  "WFActionParameterFilterPrefix": 0,
                  "WFActionParameterFilterTemplates": [
                     {
                        "WFConditionalActionString": "Savings",
                        "WFCondition": 4,
                        "WFInput": {
                           "Type": "Variable",
                           "Variable": {
                              "Value": {
                                 "VariableName": "category",
                                 "Type": "Variable"
                              },
                              "WFSerializationType": "WFTextTokenAttachment"
                           }
                        }
                     },
                     {
                        "WFInput": {
                           "Type": "Variable",
                           "Variable": {
                              "Value": {
                                 "VariableName": "category",
                                 "Type": "Variable"
                              },
                              "WFSerializationType": "WFTextTokenAttachment"
                           }
                        },
                        "WFCondition": 4,
                        "WFConditionalActionString": "Salary"
                     },
                     {
                        "WFConditionalActionString": "Bonus",
                        "WFInput": {
                           "Type": "Variable",
                           "Variable": {
                              "Value": {
                                 "VariableName": "category",
                                 "Type": "Variable"
                              },
                              "WFSerializationType": "WFTextTokenAttachment"
                           }
                        },
                        "WFCondition": 4
                     }
                  ],
                  "WFContentPredicateBoundedDate": false
               },
               "WFSerializationType": "WFContentPredicateTableTemplate"
            },
            "GroupingIdentifier": "6AECA021-069A-4755-8003-06E6F4DCE108",
            "WFControlFlowMode": 0
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Bank%20Transfer",
            "UUID": "4E6BA2AE-BA00-4BF6-B2AA-BA4060909A53"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "4E6BA2AE-BA00-4BF6-B2AA-BA4060909A53",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFControlFlowMode": 2,
            "GroupingIdentifier": "6AECA021-069A-4755-8003-06E6F4DCE108",
            "UUID": "CDE0ECF0-0200-4435-A9B7-61D4CB749D8C"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Type": "Variable",
               "Variable": {
                  "Value": {
                     "VariableName": "category",
                     "Type": "Variable"
                  },
                  "WFSerializationType": "WFTextTokenAttachment"
               }
            },
            "WFControlFlowMode": 0,
            "WFConditionalActionString": "PayNow",
            "GroupingIdentifier": "D51F6B8D-A3C2-427E-86DE-C4FC47DF1F81",
            "WFCondition": 4
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "PayNow",
            "UUID": "8DE28365-6C4B-4C67-BD41-A7FDA58D02A1"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "8DE28365-6C4B-4C67-BD41-A7FDA58D02A1",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFControlFlowMode": 2,
            "GroupingIdentifier": "D51F6B8D-A3C2-427E-86DE-C4FC47DF1F81",
            "UUID": "61A543E6-6E15-48E2-AB57-31D281CFD14D"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Type": "Variable",
               "Variable": {
                  "Value": {
                     "VariableName": "category",
                     "Type": "Variable"
                  },
                  "WFSerializationType": "WFTextTokenAttachment"
               }
            },
            "WFControlFlowMode": 0,
            "WFConditionalActionString": "Deposit",
            "GroupingIdentifier": "A2397D1E-25C3-4682-A13E-D801AE01B893",
            "WFCondition": 4
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Cash",
            "UUID": "296DBEB9-16F4-41FA-AFC2-CFCC1E265729"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "296DBEB9-16F4-41FA-AFC2-CFCC1E265729",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFControlFlowMode": 2,
            "GroupingIdentifier": "A2397D1E-25C3-4682-A13E-D801AE01B893",
            "UUID": "25C15608-A71F-4285-9083-8BF3ECE01083"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Type": "Variable",
               "Variable": {
                  "Value": {
                     "VariableName": "category",
                     "Type": "Variable"
                  },
                  "WFSerializationType": "WFTextTokenAttachment"
               }
            },
            "WFControlFlowMode": 0,
            "WFConditionalActionString": "Other",
            "GroupingIdentifier": "47FB68C6-6BCB-4ACF-A1C6-C4F1D20FBBEC",
            "WFCondition": 4
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuPrompt": "Mode: ",
            "WFControlFlowMode": 0,
            "WFMenuItems": [
               "PayNow",
               "Bank Transfer",
               "Cash"
            ],
            "GroupingIdentifier": "2DA87C77-DA84-49C8-9618-F12A9756EB51"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "PayNow",
            "GroupingIdentifier": "2DA87C77-DA84-49C8-9618-F12A9756EB51",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "PayNow",
            "UUID": "76B86A89-2D56-4769-A8B3-752EB7284CEA"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "76B86A89-2D56-4769-A8B3-752EB7284CEA",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Bank Transfer",
            "GroupingIdentifier": "2DA87C77-DA84-49C8-9618-F12A9756EB51",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Bank Transfer",
            "UUID": "357793FB-2515-4886-8727-F795AEE7015F"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "357793FB-2515-4886-8727-F795AEE7015F",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Cash",
            "GroupingIdentifier": "2DA87C77-DA84-49C8-9618-F12A9756EB51",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "Cash",
            "UUID": "579AC1DE-C0E2-4189-938D-640D4045EEDE"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "579AC1DE-C0E2-4189-938D-640D4045EEDE",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "GroupingIdentifier": "2DA87C77-DA84-49C8-9618-F12A9756EB51",
            "WFControlFlowMode": 2
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "GroupingIdentifier": "47FB68C6-6BCB-4ACF-A1C6-C4F1D20FBBEC",
            "WFControlFlowMode": 2
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "GroupingIdentifier": "A6305465-0182-4EA4-9B67-0C64F466F347",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuPrompt": "Payment Mode: ",
            "WFControlFlowMode": 0,
            "WFMenuItems": [
               "NetsQR",
               "PayNow",
               "Visa",
               "Cash"
            ],
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "NetsQR",
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "NetsQR",
            "UUID": "37C5D09A-98D6-484C-9AEC-C95CAC75D5EF"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "37C5D09A-98D6-484C-9AEC-C95CAC75D5EF",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "PayNow",
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "PayNow",
            "UUID": "EEAE7966-0AE9-4BE7-A510-99A981CC7534"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "EEAE7966-0AE9-4BE7-A510-99A981CC7534",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Visa",
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "UUID": "C0E463EC-5809-4FD1-A8E7-4C88CB9E80B9",
            "WFTextActionText": "Visa"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "C0E463EC-5809-4FD1-A8E7-4C88CB9E80B9",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "WFMenuItemTitle": "Cash",
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A",
            "WFControlFlowMode": 1
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "UUID": "A6D318CF-9CBF-47BA-BE13-443E4E692A53",
            "WFTextActionText": "Cash"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "A6D318CF-9CBF-47BA-BE13-443E4E692A53",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "account"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.choosefrommenu",
         "WFWorkflowActionParameters": {
            "UUID": "F6A509C5-0A2A-4910-8B90-696381628ED4",
            "GroupingIdentifier": "D4497B5D-BE97-486C-B2B1-36A772E8091A",
            "WFControlFlowMode": 2
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
         "WFWorkflowActionParameters": {
            "UUID": "31C8AAB7-F59E-4E6C-86F5-8D12B1E87C44",
            "GroupingIdentifier": "A6305465-0182-4EA4-9B67-0C64F466F347",
            "WFControlFlowMode": 2
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.ask",
         "WFWorkflowActionParameters": {
            "WFAskActionPrompt": "Description: ",
            "WFAskActionDefaultAnswer": "",
            "UUID": "75254D9E-C20B-4090-A1B3-C0E4F02A237C"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.detect.text",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "75254D9E-C20B-4090-A1B3-C0E4F02A237C",
                  "Type": "ActionOutput",
                  "OutputName": "Ask for Input"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "UUID": "EE13B7F8-A129-4002-9BB0-031809E170E8"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.urlencode",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "string": "\uFFFC",
                  "attachmentsByRange": {
                     "{0, 1}": {
                        "OutputUUID": "EE13B7F8-A129-4002-9BB0-031809E170E8",
                        "Type": "ActionOutput",
                        "OutputName": "Text"
                     }
                  }
               },
               "WFSerializationType": "WFTextTokenString"
            },
            "UUID": "56D622A7-E990-4A41-80F6-FA9BD202D8E4"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "56D622A7-E990-4A41-80F6-FA9BD202D8E4",
                  "Type": "ActionOutput",
                  "OutputName": "URL Encoded Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "detail"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": "AKfycbwtxhqmW0rY3MaWbpFlP6P1CoPLezE8xV3e_JTEt8rksEmC8Q4wKH5T2fvpSdvYCRcd",
            "UUID": "60775F11-883F-427C-8244-D91AA9E534E6"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "OutputUUID": "60775F11-883F-427C-8244-D91AA9E534E6",
                  "Type": "ActionOutput",
                  "OutputName": "Text"
               },
               "WFSerializationType": "WFTextTokenAttachment"
            },
            "WFVariableName": "webappid"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
         "WFWorkflowActionParameters": {
            "WFTextActionText": {
               "Value": {
                  "string": "https://script.google.com/macros/s/\uFFFC/exec?amount=\uFFFC&expenditure=\uFFFC&account=\uFFFC&category=\uFFFC&detail=\uFFFC",
                  "attachmentsByRange": {
                     "{49, 1}": {
                        "VariableName": "amount",
                        "Type": "Variable",
                        "Aggrandizements": [
                           {
                              "Type": "WFCoercionVariableAggrandizement",
                              "CoercionItemClass": "WFStringContentItem"
                           }
                        ]
                     },
                     "{35, 1}": {
                        "VariableName": "webappid",
                        "Type": "Variable"
                     },
                     "{63, 1}": {
                        "VariableName": "expenditure",
                        "Type": "Variable"
                     },
                     "{93, 1}": {
                        "VariableName": "detail",
                        "Type": "Variable"
                     },
                     "{73, 1}": {
                        "VariableName": "account",
                        "Type": "Variable",
                        "Aggrandizements": [
                           {
                              "Type": "WFCoercionVariableAggrandizement",
                              "CoercionItemClass": "WFStringContentItem"
                           }
                        ]
                     },
                     "{84, 1}": {
                        "VariableName": "category",
                        "Type": "Variable",
                        "Aggrandizements": [
                           {
                              "Type": "WFCoercionVariableAggrandizement",
                              "CoercionItemClass": "WFStringContentItem"
                           }
                        ]
                     }
                  }
               },
               "WFSerializationType": "WFTextTokenString"
            },
            "UUID": "35C7D3DE-168A-4506-AD60-CE435563EA3D"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.detect.link",
         "WFWorkflowActionParameters": {
            "WFInput": {
               "Value": {
                  "string": "\uFFFC",
                  "attachmentsByRange": {
                     "{0, 1}": {
                        "OutputUUID": "35C7D3DE-168A-4506-AD60-CE435563EA3D",
                        "Type": "ActionOutput",
                        "OutputName": "Text"
                     }
                  }
               },
               "WFSerializationType": "WFTextTokenString"
            },
            "UUID": "DF92FCED-D9B5-4B73-956D-9D0A67146F35"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.downloadurl",
         "WFWorkflowActionParameters": {
            "Advanced": true,
            "WFHTTPHeaders": {
               "Value": {
                  "WFDictionaryFieldValueItems": []
               },
               "WFSerializationType": "WFDictionaryFieldValue"
            },
            "ShowHeaders": true,
            "UUID": "77D8169A-C485-4E94-BD43-7A0FFD07D257",
            "WFURL": {
               "Value": {
                  "string": "\uFFFC",
                  "attachmentsByRange": {
                     "{0, 1}": {
                        "OutputUUID": "DF92FCED-D9B5-4B73-956D-9D0A67146F35",
                        "Type": "ActionOutput",
                        "OutputName": "URLs"
                     }
                  }
               },
               "WFSerializationType": "WFTextTokenString"
            },
            "WFHTTPMethod": "GET"
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.showresult",
         "WFWorkflowActionParameters": {
            "Text": {
               "Value": {
                  "string": "\uFFFC",
                  "attachmentsByRange": {
                     "{0, 1}": {
                        "OutputUUID": "77D8169A-C485-4E94-BD43-7A0FFD07D257",
                        "Type": "ActionOutput",
                        "OutputName": "Contents of URL"
                     }
                  }
               },
               "WFSerializationType": "WFTextTokenString"
            }
         }
      },
      {
         "WFWorkflowActionIdentifier": "is.workflow.actions.vibrate",
         "WFWorkflowActionParameters": {
            "WFVibrateHapticType": "Up Direction"
         }
      }
   ],
   "WFWorkflowInputContentItemClasses": [
      "WFAppStoreAppContentItem",
      "WFArticleContentItem",
      "WFContactContentItem",
      "WFDateContentItem",
      "WFEmailAddressContentItem",
      "WFGenericFileContentItem",
      "WFImageContentItem",
      "WFiTunesProductContentItem",
      "WFLocationContentItem",
      "WFDCMapsLinkContentItem",
      "WFAVAssetContentItem",
      "WFPDFContentItem",
      "WFPhoneNumberContentItem",
      "WFRichTextContentItem",
      "WFSafariWebPageContentItem",
      "WFStringContentItem",
      "WFURLContentItem"
   ],
   "WFWorkflowTypes": [
      "Watch",
      "NCWidget"
   ],
   "WFWorkflowImportQuestions": [
      {
         "ParameterKey": "WFTextActionText",
         "Category": "Parameter",
         "ActionIndex": 48,
         "Text": "Webappid?"
      }
   ],
   "WFQuickActionSurfaces": [],
   "WFWorkflowHasShortcutInputVariables": false
}
```
