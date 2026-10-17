import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

def calldata_compat(method=None,args=None,kwargs=None):
 result={}
 if method is not None: result['method']=method
 if args: result['args']=args
 if kwargs: result['kwargs']=kwargs
 return result
contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(encoding='utf-8'); KEY=re.search(r'^ACCOUNT_2_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip()
client=create_client(chain=studionet,account=create_account(account_private_key=KEY)); address=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
def finalized(name,args,expected='SUCCESS'):
 tx=client.write_contract(address=address,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True)
 receipt=client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leader=(receipt.get('consensus_data',{}).get('leader_receipt') or [{}])[0]
 assert receipt.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')==expected,receipt
 return str(tx),leader
stamp=str(int(time.time())); forecast_id='PRESS-'+stamp; forecast='https://cdn.jsdelivr.net/gh/warnedwarn/probability-press@main/fixtures/forecast.md'; outcome='https://raw.githack.com/warnedwarn/probability-press/main/fixtures/outcome.md'
open_tx,_=finalized('open_forecast',[forecast_id,'Berth 4 opening','The public port notice will report Berth 4 open for commercial arrivals.','Mark OCCURRED only if the outcome bulletin explicitly states that Berth 4 opened for commercial arrivals on the named date.',forecast,70,1])
before=client.read_contract(address=address,function_name='get_forecast',args=[forecast_id]); duplicate_tx,duplicate_leader=finalized('open_forecast',[forecast_id,'Duplicate plate','The public port notice will report Berth 4 open for commercial arrivals.','Mark OCCURRED only if the outcome bulletin explicitly states that Berth 4 opened for commercial arrivals on the named date.',forecast,70,1],expected='ERROR'); unchanged=client.read_contract(address=address,function_name='get_forecast',args=[forecast_id]); assert before==unchanged and before['state']=='LOCKED'
resolve_tx,_=finalized('resolve_forecast',[forecast_id,outcome]); final=client.read_contract(address=address,function_name='get_forecast',args=[forecast_id]); resolution=client.read_contract(address=address,function_name='get_resolution',args=[forecast_id]); assert final['state']=='SCORED' and resolution['outcome']=='OCCURRED' and resolution['score_millis']==90,(final,resolution)
proof={'forecastId':forecast_id,'transactions':{'openForecast':open_tx,'duplicateForecastRejected':duplicate_tx,'resolveForecast':resolve_tx},'negativeExecution':duplicate_leader.get('execution_result'),'stateUnchangedAfterDuplicateRejection':before==unchanged,'forecast':final,'resolution':resolution,'fixtureDisclosure':'Both records are operator-controlled fixtures on distinct delivery hosts.'}
(ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n',encoding='utf-8'); print(json.dumps(proof,indent=2),flush=True)
