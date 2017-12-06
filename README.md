#health-check

________________


This project checks the health for a number of backend services and see if they are able to connect and get service status

The following backends are bundled into this project:

* Mongodb
* Redis
* Elasticsearch
* Kafka
* HTTP API


## Installation

```
python setup.py install
```

## Get-Start

User `health_check.HealthChecker` to create a initialize a health checker.

```
from health_check import HealthChecker

checker = HealthChecker()
checker.run()

# {'healthy': True}

```

## Checkers

### Mongodb

```
from health_check import HealthChecker
from health_check import MongodbChecker
handle = HealthChecker()
mongo_checker = MongodbChecker('mongodb', uri='mongodb://localhost:27017/test')
handle.add_checker(mongo_checker)
handle.run()

# {'mongodb': {'name': 'mongodb', 'healthy': True, 'status': {'db': 'test', 'collections': 3, 'objects': 6, 'avgObjSize': 58.666666666666664, 'dataSize': 352.0, 'storageSize': 20480.0, 'numExtents': 3, 'indexes': 1, 'indexSize': 8176.0, 'fileSize': 67108864.0, 'nsSizeMB': 16, 'extentFreeList': {'num': 0, 'totalSize': 0}, 'dataFileVersion': {'major': 4, 'minor': 22}, 'ok': 1.0}, 'time_cost': 0.07084989547729492}, 'healthy': True}
```

### Redis
```
from health_check import HealthChecker
from health_check import RedisChecker
handle = HealthChecker()
redis_checker = RedisChecker('redis', host='localhost')
handle.add_checker(redis_checker)
handle.run()

# {'redis': {'name': 'redis', 'healthy': True, 'status': {'redis_version': '4.0.1', 'redis_git_sha1': 0, 'redis_git_dirty': 0, 'redis_build_id': 'f37081b32886670b', 'redis_mode': 'standalone', 'os': 'Darwin 17.2.0 x86_64', 'arch_bits': 64, 'multiplexing_api': 'kqueue', 'atomicvar_api': 'atomic-builtin', 'gcc_version': '4.2.1', 'process_id': 11789, 'run_id': '94ce4c6683530f889fad7b095d21ed8edaba22ae', 'tcp_port': 6379, 'uptime_in_seconds': 85309, 'uptime_in_days': 0, 'hz': 10, 'lru_clock': 2602149, 'executable': '/Users/xuxu/workspace/service/redis/redis-server', 'config_file': '/Users/xuxu/workspace/service/redis/redis.conf', 'connected_clients': 1, 'client_longest_output_list': 0, 'client_biggest_input_buf': 0, 'blocked_clients': 0, 'used_memory': 1019248, 'used_memory_human': '995.36K', 'used_memory_rss': 245760, 'used_memory_rss_human': '240.00K', 'used_memory_peak': 1036560, 'used_memory_peak_human': '1012.27K', 'used_memory_peak_perc': '98.33%', 'used_memory_overhead': 1014126, 'used_memory_startup': 963328, 'used_memory_dataset': 5122, 'used_memory_dataset_perc': '9.16%', 'total_system_memory': 8589934592, 'total_system_memory_human': '8.00G', 'used_memory_lua': 37888, 'used_memory_lua_human': '37.00K', 'maxmemory': 0, 'maxmemory_human': '0B', 'maxmemory_policy': 'noeviction', 'mem_fragmentation_ratio': 0.24, 'mem_allocator': 'libc', 'active_defrag_running': 0, 'lazyfree_pending_objects': 0, 'loading': 0, 'rdb_changes_since_last_save': 0, 'rdb_bgsave_in_progress': 0, 'rdb_last_save_time': 1512466280, 'rdb_last_bgsave_status': 'ok', 'rdb_last_bgsave_time_sec': -1, 'rdb_current_bgsave_time_sec': -1, 'rdb_last_cow_size': 0, 'aof_enabled': 0, 'aof_rewrite_in_progress': 0, 'aof_rewrite_scheduled': 0, 'aof_last_rewrite_time_sec': -1, 'aof_current_rewrite_time_sec': -1, 'aof_last_bgrewrite_status': 'ok', 'aof_last_write_status': 'ok', 'aof_last_cow_size': 0, 'total_connections_received': 8, 'total_commands_processed': 8, 'instantaneous_ops_per_sec': 0, 'total_net_input_bytes': 132, 'total_net_output_bytes': 36796, 'instantaneous_input_kbps': 0.0, 'instantaneous_output_kbps': 0.0, 'rejected_connections': 0, 'sync_full': 0, 'sync_partial_ok': 0, 'sync_partial_err': 0, 'expired_keys': 0, 'evicted_keys': 0, 'keyspace_hits': 0, 'keyspace_misses': 0, 'pubsub_channels': 0, 'pubsub_patterns': 0, 'latest_fork_usec': 0, 'migrate_cached_sockets': 0, 'slave_expires_tracked_keys': 0, 'active_defrag_hits': 0, 'active_defrag_misses': 0, 'active_defrag_key_hits': 0, 'active_defrag_key_misses': 0, 'role': 'master', 'connected_slaves': 0, 'master_replid': '70b244d70b24eb162fe9e873ad0b03d440f45ecc', 'master_replid2': 0, 'master_repl_offset': 0, 'second_repl_offset': -1, 'repl_backlog_active': 0, 'repl_backlog_size': 1048576, 'repl_backlog_first_byte_offset': 0, 'repl_backlog_histlen': 0, 'used_cpu_sys': 18.88, 'used_cpu_user': 8.86, 'used_cpu_sys_children': 0.0, 'used_cpu_user_children': 0.0, 'cluster_enabled': 0, 'db1': {'keys': 22, 'expires': 0, 'avg_ttl': 0}}, 'time_cost': 0.056463003158569336}, 'healthy': True}
```

### Kafka
```
```

### Elasticsearch
```
```

### HTTP
```
```

## How to create a Checker

```
from health_check import HealthChecker
health = HealthChecker()

from health_check import BaseBackendChecker

class MyChecker(BaseBackendChecker):

	def check_status(self):
		return 'ok'
		
health.add_checker(MyChecker('my-checker'))
health.run()

# {'healthy': True, 'my-checker': {'name': 'my-checker', 'healthy': True, 'status': 'ok', 'time_cost': 8.821487426757812e-06}}

```



