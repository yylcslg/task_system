import json

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

def query_collection(w, a):
    url = 'https://api.element.market/graphql?args=AssetsListFromUser'

    headers = {
        'Authority': 'api.element.market',
        'Method': 'POST',
        'Path': '/graphql?args=AssetsListFromUser',
        'Scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '3469',
        'Content-Type': 'application/json; charset=utf-8',
        'Lang': 'zh-CN',
        'Languagetype': 'zh-CN',
        'Origin': 'https://element.market',
        'Referer': 'https://element.market/',
        'Region': 'other',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Api-Key': 'zQbYj7RhC1VHIBdWU63ki5AJKXloamDT',
        'X-Api-Sign': '469ba3e99ea9913ffd7fa82829a766701a109023d0bbedf75c7d36a631cab2b9.9008.1697700268',
        'X-Query-Args': 'AssetsListFromUser',
        'X-Viewer-Addr': '0x3141ccbcc38fecb363d52f3a03eec86ccdbe34eb',
        'X-Viewer-Chainmid': '701'
    }

    payload = {"operationName": "AssetsListFromUser",
  "variables": {
    "realtime": True,
    "thirdStandards": [
      "element-ex-v3"
    ],
    "sortAscending": False,
    "sortBy": "RecentlyTransferred",
    "ownerAddress": "0x3141ccbcc38fecb363d52f3a03eec86ccdbe34eb",
    "first": 50,
    "uiFlag": "COLLECTED",
    "blockChains": [
      {
        "chain": "zksync",
        "chainId": "0x144"
      }
    ],
    "account": {
      "address": "0x3141ccbcc38fecb363d52f3a03eec86ccdbe34eb",
      "blockChain": {
        "chain": "zksync",
        "chainId": "0x144"
      }
    },
    "constantWhenERC721": 1
  },
  "query": "query AssetsListFromUser($before: String, $after: String, $first: Int, $last: Int, $querystring: String, $categorySlugs: [String!], $collectionSlugs: [String!], $sortBy: SearchSortBy, $sortAscending: Boolean, $toggles: [SearchToggle!], $ownerAddress: Address, $creatorAddress: Address, $blockChains: [BlockChainInput!], $paymentTokens: [String!], $priceFilter: PriceFilterInput, $stringTraits: [StringTraitInput!], $contractAliases: [String!], $thirdStandards: [String!], $uiFlag: SearchUIFlag, $account: IdentityInput, $constantWhenERC721: Int) {\n  search(\n    \n    before: $before\n    after: $after\n    first: $first\n    last: $last\n    search: {querystring: $querystring, categorySlugs: $categorySlugs, collectionSlugs: $collectionSlugs, sortBy: $sortBy, sortAscending: $sortAscending, toggles: $toggles, ownerAddress: $ownerAddress, creatorAddress: $creatorAddress, blockChains: $blockChains, paymentTokens: $paymentTokens, priceFilter: $priceFilter, stringTraits: $stringTraits, contractAliases: $contractAliases, uiFlag: $uiFlag}\n  ) {\n    totalCount\n    edges {\n      cursor\n      node {\n        asset {\n          chain\n          chainId\n          contractAddress\n          tokenId\n          tokenType\n          name\n          imagePreviewUrl\n          animationUrl\n          rarityRank\n          isFavorite\n          ownedQuantity(viewer: $account, constantWhenERC721: $constantWhenERC721)\n          orderData(standards: $thirdStandards, account: $account) {\n            bestAsk {\n              ...BasicOrder\n            }\n            bestBid {\n              ...BasicOrder\n            }\n          }\n          assetEventData {\n            lastSale {\n              lastSaleDate\n              lastSalePrice\n              lastSalePriceUSD\n              lastSaleTokenContract {\n                name\n                address\n                icon\n                decimal\n                accuracy\n              }\n            }\n          }\n          marketStandards(account: $account) {\n            count\n            standard\n            floorPrice\n          }\n          collection {\n            name\n            isVerified\n            slug\n            imageUrl\n            royaltyAddress\n            royalty\n            royaltyFeeEnforced\n            contracts {\n              blockChain {\n                chain\n                chainId\n              }\n            }\n          }\n          suspiciousStatus\n          uri\n        }\n      }\n    }\n    pageInfo {\n      hasPreviousPage\n      hasNextPage\n      startCursor\n      endCursor\n    }\n  }\n}\n\nfragment BasicOrder on OrderV3Type {\n  __typename\n  chain\n  chainId\n  chainMId\n  expirationTime\n  listingTime\n  maker\n  taker\n  side\n  saleKind\n  paymentToken\n  quantity\n  priceBase\n  priceUSD\n  price\n  standard\n  contractAddress\n  tokenId\n  schema\n  extra\n  paymentTokenCoin {\n    name\n    address\n    icon\n    chain\n    chainId\n    decimal\n    accuracy\n  }\n}\n"
}
    params = {'args':'AssetsListFromUser'}
    rsp = w.session.request(method='post', url=url, headers=headers,data=json.dumps(payload))

    print(rsp.status_code, rsp.content)




a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.ZKS_ERA, gas_flag=False)

query_collection(w, a1)