
"""
  @apiDefine admin Admin access rights needed.
  Optionally you can write here further Informations about the permission.
 
  An "apiDefinePermission"-block can have an "apiVersion", so you can attach the block to a specific version.
 
  @apiVersion 0.1.0
"""

"""
  @api {get} /cluster/ List Clusters
  @apiName Cluster
  @apiVersion 0.1.0
  @apiGroup Cluster
  @apiPermission admin
 
  @apiSuccess {Date}     update_time   Update Date.
  @apiSuccess {String}   id            Uuid of Cluster.
  @apiSuccess {String}   name          Cluster Name.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      [
        {
            "update_time": "2014-11-06T21:15:15.168126+00:00",
            "id": "dce20d46-f010-4883-988c-4a6d8bd15793",
            "name": "ceph_fake"
        }
      ]
"""
def Clusters() { return; }

"""
  @api {post} /cluster/ Create Cluster
  @apiName CreateCluster
  @apiVersion 0.1.0
  @apiGroup Cluster
  @apiPermission admin

  @apiParam {Object} topology Topology of Cluster

  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      [
        {
            "update_time": "2014-11-06T21:15:15.168126+00:00",
            "id": "dce20d46-f010-4883-988c-4a6d8bd15793",
            "name": "ceph_fake"
        }
      ]
"""
def CreateCluster() { return; }


"""
  @api {get} /cluster/${uuid} Get Cluster Status 
  @apiName getCluster
  @apiVersion 0.1.0
  @apiGroup Cluster
  @apiPermission none
 
  @apiParam {String} uuid UUID of Cluster.
 
  @apiSuccess {Date}     update_time   Update Date.
  @apiSuccess {String}   id            Uuid of Cluster.
  @apiSuccess {String}   name          Cluster Name.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      {
          "update_time": "2014-11-06T21:15:15.168126+00:00",
          "id": "dce20d46-f010-4883-988c-4a6d8bd15793",
          "name": "ceph_fake"
      }
"""
def getCluster() { return; }

"""
  @api {post} /cluster/${uuid}/pg List PGs
  @apiName listPg
  @apiVersion 0.1.0
  @apiGroup Pg
  @apiPermission none
 
  @apiParam {String} uuid UUID of Cluster.
 
  @apiSuccess {String}   id             PG ID.
  @apiSuccess {String}   state          PG State.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      [
        {
          "pgid": "7.e",
          "state": "active+clean"
        },
        {
          "pgid": "7.f",
          "state": "active+clean"
        }
      ]
"""
def Pg() { return; }

"""
  @api {post} /cluster/${uuid}/pg/${pg_id}/scrub Scrub Pg
  @apiName scrubPg
  @apiVersion 0.1.0
  @apiGroup Pg
  @apiPermission none
 
  @apiParam {String} uuid             UUID of Cluster.
  @apiParam {String} pgid             PG ID.
 
  @apiSuccess {String}   id             PG ID.
  @apiSuccess {String}   state          PG State.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      {
        "pgid": "7.f",
        "state": "active+scrubbing"
      }
"""
def scrubPg() { return; }

"""
  @api {post} /cluster/${uuid}/pg/${pg_id}/deepscrub Deep Scrub Pg
  @apiName deepscrubPg
  @apiVersion 0.1.0
  @apiGroup Pg
  @apiPermission none
 
  @apiParam {String} uuid             UUID of Cluster.
  @apiParam {String} pgid             PG ID.
 
  @apiSuccess {String}   id             PG ID.
  @apiSuccess {String}   state          PG State.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      {
        "pgid": "7.f",
        "state": "active+deepscrubbing"
      }
"""
def deppscrubPg() { return; }

"""
  @api {post} /cluster/${uuid}/pg/${pg_id}/repair Repair Pg
  @apiName repairPg
  @apiVersion 0.1.0
  @apiGroup Pg
  @apiPermission none
 
  @apiParam {String} uuid             UUID of Cluster.
  @apiParam {String} pgid             PG ID.
 
  @apiSuccess {String}   id             PG ID.
  @apiSuccess {String}   state          PG State.
 
  @apiSuccessExample Response:
      HTTP/1.1 200 OK
      {
        "pgid": "7.f",
        "state": "active+repair"
      }
"""
def repairPg() { return; }

"""
  @api {get} /cluster/${uuid}/crush_map Get Crushmap 
  @apiName getCrushMap
  @apiVersion 0.1.0
  @apiGroup Crush
  @api {get} /cluster/${uuid}/crush_map Get Crushmap 
  @apiName getCrushMap
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
 
  @apiSuccess {String}crushmap Crush Map 
 
  @apiSuccessExample SuccessReponse:
      HTTP/1.1 200 OK
      {
        "\n# begin crush map\ntunable choose_local_fallback_tries 5\ntunable chooseleaf_descend_once 0\ntunable choose_local_tries 2\ntunable choose_total_tries 19\n\n# devices\ndevice 0 osd.0\ndevice 1 osd.1\ndevice 2 osd.2\ndevice 3 osd.3\ndevice 4 osd.4\n\n# types\ntype 0 osd\ntype 1 host\ntype 2 rack\ntype 3 row\ntype 4 room\ntype 5 datacenter\ntype 6 root\n\n# buckets\nhost gravel3 {\n    id -4       # do not change unnecessarily\n    # weight 0.910\n    alg straw\n    hash 0  # rjenkins1\n    item osd.2 weight 0.910\n}\nhost gravel2 {\n    id -3       # do not change unnecessarily\n    # weight 0.910\n    alg straw\n    hash 0  # rjenkins1\n    item osd.1 weight 0.910\n}\nhost gravel1 {\n    id -2       # do not change unnecessarily\n    # weight 3.020\n    alg straw\n    hash 0  # rjenkins1\n    item osd.0 weight 0.910\n    item osd.3 weight 1.820\n    item osd.4 weight 0.290\n}\nroot default {\n    id -1       # do not change unnecessarily\n    # weight 4.840\n    alg straw\n    hash 0  # rjenkins1\n    item gravel1 weight 3.020\n    item gravel2 weight 0.910\n    item gravel3 weight 0.910\n}\n\n# rules\nrule data {\n    ruleset 0\n    type replicated\n    min_size 1\n    max_size 10\n    step take default\n    step chooseleaf firstn 0 type host\n    step emit\n}\nrule metadata {\n    ruleset 1\n    type replicated\n    min_size 1\n    max_size 10\n    step take default\n    step chooseleaf firstn 0 type host\n    step emit\n}\nrule rbd {\n    ruleset 2\n    type replicated\n    min_size 1\n    max_size 10\n    step take default\n    step chooseleaf firstn 0 type host\n    step emit\n}\n\n# end crush map\n"
      }
"""
def getCrushMap(return;)

"""
  @api {get} /cluster/${uuid}/crush_node List Crush Node
  @apiName CrushNode
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
  
  @apiSuccess {stirng} bucket_type Buckets facilitate a hierarchy of nodes and leaves. Node (or non-leaf) buckets typically represent physical locations in a hierarchy. e.g. host, rack, datacenter
  @apiSuccess {String} unique name
  @apiSuccess {Number} unique ID 
  @apiSuccess {Number} the relative capacity/capability of the item(s)
  @apiSuccess {String} bucket algorithm
  @apiSuccess {Number} hash algorithm
  @apiSuccess {Field} A bucket may have one or more items. The items may consist of node buckets or leaves. Items may have a weight that reflects the relative weight of the item.
 
  @apiSuccessExample SuccessReponse:
      HTTP/1.1 200 OK
      {
        [
          {
            "bucket_type": "root",
            "hash": "rjenkins1",
            "name": "default",
            "weight": 4.8399505615234375,
            "alg": "straw",
            "items": [
              {
                "id": -2,
                "weight": 3.0199737548828125,
                "pos": 0
              },
              {
                "id": -3,
                "weight": 0.9099884033203125,
                "pos": 1
              },
              {
                "id": -4,
                "weight": 0.9099884033203125,
                "pos": 2
              }
            ],
            "id": -1
          },
          {
            "bucket_type": "host",
            "hash": "rjenkins1",
            "name": "gravel1",
            "weight": 3.0199737548828125,
            "alg": "straw",
            "items": [
              {
                "id": 0,
                "weight": 0.9099884033203125,
                "pos": 0
              },
              {
                "id": 3,
                "weight": 1.8199920654296875,
                "pos": 1
              },
              {
                "id": 4,
                "weight": 0.2899932861328125,
                "pos": 2
              }
            ],
            "id": -2
          },
          {
            "bucket_type": "host",
            "hash": "rjenkins1",
            "name": "gravel2",
            "weight": 0.9099884033203125,
            "alg": "straw",
            "items": [
              {
                "id": 1,
                "weight": 0.9099884033203125,
                "pos": 0
              }
            ],
            "id": -3
          },
          {
            "bucket_type": "host",
            "hash": "rjenkins1",
            "name": "gravel3",
            "weight": 0.9099884033203125,
            "alg": "straw",
            "items": [
              {
                "id": 2,
                "weight": 0.9099884033203125,
                "pos": 0
              }
            ],
            "id": -4
          }
        ]
      }
"""
def CrushNode(return;)

"""
  @api {get} /cluster/${uuid}/crush_node/${node_id} Get a Crush Node
  @apiName getCrushNode
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id Node ID
 
  @apiSuccess {stirng} bucket_type Buckets facilitate a hierarchy of nodes and leaves. Node (or non-leaf) buckets typically represent physical locations in a hierarchy. e.g. host, rack, datacenter
  @apiSuccess {String} name unique name
  @apiSuccess {Number} id unique ID 
  @apiSuccess {Number} weight the relative capacity/capability of the item(s)
  @apiSuccess {String} alg bucket algorithm
  @apiSuccess {Number} hash hash algorithm
  @apiSuccess {Field}  items A bucket may have one or more items. The items may consist of node buckets or leaves. Items may have a weight that reflects the relative weight of the item.
 
  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "bucket_type": "root",
        "hash": "rjenkins1",
        "name": "default",
        "weight": 4.8399505615234375,
        "alg": "straw",
        "items": [
          {
            "id": -2,
            "weight": 3.0199737548828125,
            "pos": 0
          },
          {
            "id": -3,
            "weight": 0.9099884033203125,
            "pos": 1
          },
          {
            "id": -4,
            "weight": 0.9099884033203125,
            "pos": 2
          }
        ],
        "id": -1
      }
"""
def getCrushNode(){return;}

"""
  @api {get} /cluster/${uuid}/crush_type List Crush Type
  @apiName CrushType
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
 
  @apiSuccess {Number} id unique ID 
  @apiSuccess {String} name unique name
 
  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        [
           {
             "id": 0,
             "name": "osd"
           },
           {
             "id": 1,
             "name": "host"
           },
           {
             "id": 2,
             "name": "rack"
           },
           {
             "id": 3,
             "name": "row"
           },
           {
             "id": 4,
             "name": "room"
           },
           {
             "id": 5,
             "name": "datacenter"
           },
           {
             "id": 6,
             "name": "root"
           }
         ]
      }
"""
def CrushType(){return;}

"""
  @api {get} /cluster/${uuid}/crush_type/${type_id} Get a Crush Type
  @apiName getCrushType
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id Type ID

  @apiSuccess {Number} id unique ID
  @apiSuccess {String} name unique name

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "id": 1,
        "name": "host"
      }
"""
def getCrushType(){return;}

"""
  @api {get} /cluster/${uuid}/crush_rule List Crush Rules
  @apiName CrushRuleSet
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin

  @apiParam {String} uuid UUID of cluster

  @apiSuccess {Number} id Rule Set ID
  @apiSuccess {Object} rules Rules
  @apiSuccessExample {json} SuccessReponse:
    HTTP/1.1 200 OK
    [
       {
         "rules": [
           {
             "name": "data",
             "osd_count": 12,
             "min_size": 1,
             "steps": [
               {
                 "item": -1,
                 "op": "take"
               },
               {
                 "num": 0,
                 "type": "host",
                 "op": "chooseleaf_firstn"
               },
               {
                 "op": "emit"
               }
             ],
             "ruleset": 0,
             "type": "replicated",
             "id": 0,
             "max_size": 10
           }
         ],
         "id": 0
       },
       {
         "rules": [
           {
             "name": "metadata",
             "osd_count": 12,
             "min_size": 1,
             "steps": [
               {
                 "item": -1,
                 "op": "take"
               },
               {
                 "num": 0,
                 "type": "host",
                 "op": "chooseleaf_firstn"
               },
               {
                 "op": "emit"
               }
             ],
             "ruleset": 1,
             "type": "replicated",
             "id": 1,
             "max_size": 10
           }
         ],
         "id": 1
       },
       {
         "rules": [
           {
             "name": "rbd",
             "osd_count": 12,
             "min_size": 1,
             "steps": [
               {
                 "item": -1,
                 "op": "take"
               },
               {
                 "num": 0,
                 "type": "host",
                 "op": "chooseleaf_firstn"
               },
               {
                 "op": "emit"
               }
             ],
             "ruleset": 2,
             "type": "replicated",
             "id": 2,
             "max_size": 10
           }
         ],
         "id": 2
       }
     ]
"""
def CrushRule(){return;}

"""
  @api {get} /cluster/${uuid}/crush_rule/${ruleset_id} Get Crush Rule
  @apiName getCrushRule
  @apiVersion 0.1.0
  @apiGroup Crush
  @apiPermission admin

  @apiParam {String} uuid UUID of cluster
  @apiParam {Number} ruleset_id RuleSet ID

  @apiSuccess {Number} id Rule Set ID
  @apiSuccess {String} name Human readable name
  @apiSuccess {Number} ruleset ID of the CRUSH ruleset of which this rule is a member
  @apiSuccess {String} type Data redundancy type (one of replicated, erasure)
  @apiSuccess {Number} min_size If a pool makes more replicas than this number, CRUSH will NOT select this rule
  @apiSuccess {Number} max_size If a pool makes fewer replicas than this number, CRUSH will NOT select this rule
  @apiSuccess {Object} step List of operations used to select OSDs
  @apiSuccess {Number} osd_count Number of OSDs which are used for data placement

  @apiSuccessExample {json} SuccessReponse:
    HTTP/1.1 200 OK
    {
      "name": "data",
      "osd_count": 12,
      "min_size": 1,
      "steps": [
        {
          "item": -1,
          "op": "take"
        },
        {
          "num": 0,
          "type": "host",
          "op": "chooseleaf_firstn"
        },
        {
          "op": "emit"
        }
      ],
      "ruleset": 0,
      "type": "replicated",
      "id": 0,
      "max_size": 10
    },
"""
def getCrushRule(){return;}

"""
  @api {get} /cluster/${uuid}/mon List Monitors
  @apiName Mons
  @apiVersion 0.1.0
  @apiGroup Monitor
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {String}    name    Human readable name
  @apiSuccess {Number}    rank    Unique of the mon within the cluster
  @apiSuccess {Boolean}   in_quorum      True if the mon is a member of current quorum
  @apiSuccess {String}    server      	FQDN of server running the OSD
  @apiSuccess {String}    addr      IP address of monitor service

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        [
           {
             "addr": "",
             "in_quorum": true,
             "name": "figment000",
             "rank": 0,
             "server": "figment000.cluster0.com"
           },
           {
             "addr": "",
             "in_quorum": true,
             "name": "figment001",
             "rank": 1,
             "server": "figment001.cluster0.com"
           },
           {
             "addr": "",
             "in_quorum": true,
             "name": "figment002",
             "rank": 2,
             "server": "figment002.cluster0.com"
           }
         ]
      }
"""
def Mons(){return;}

"""
  @api {post} /cluster/${uuid}/mon Create Monitor
  @apiName CreateMon
  @apiVersion 0.1.0
  @apiGroup Monitor
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} mon FQDN of server

  @apiSuccess {String}    name    Human readable name
  @apiSuccess {Number}    rank    Unique of the mon within the cluster
  @apiSuccess {Boolean}   in_quorum      True if the mon is a member of current quorum
  @apiSuccess {String}    server        FQDN of server running the Mon
  @apiSuccess {String}    addr      IP address of monitor service

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        {
          "addr": "",
          "in_quorum": true,
          "name": "figment002",
          "rank": 2,
          "server": "figment002.cluster0.com"
        }
      }
"""
def CreateMon(){return;}

"""
  @api {delete} /cluster/${uuid}/mon/${mon_id} Delete Monitor
  @apiName DeleteMon
  @apiVersion 0.1.0
  @apiGroup Monitor
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} mon FQDN of server

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
      }
"""
def DeleteMon(){return;}


"""
  @api {get} /cluster/${uuid}/mon/${mon_id} Get Monitor
  @apiName getMon
  @apiVersion 0.1.0
  @apiGroup Monitor
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} mon_id ID of Monitor

  @apiSuccess {String}    name    Human readable name
  @apiSuccess {Number}    rank    Unique of the mon within the cluster
  @apiSuccess {Boolean}    in_quorum      True if the mon is a member of current quorum
  @apiSuccess {String}    server        FQDN of server running the OSD
  @apiSuccess {String}    addr      IP address of monitor service

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
       "addr": "",
        "in_quorum": true,
        "name": "figment002",
        "rank": 2,
        "server": "figment002.cluster0.com"
      }
"""
def getMon(){return;}

"""
  @api {get} /cluster/${uuid}/mon/${mon_id}/mon_status Get Monitor Status
  @apiName getMonStatus
  @apiVersion 0.1.0
  @apiGroup Monitor
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} mon_id ID of Monitor

  @apiSuccess {String}    name    Human readable name
  @apiSuccess {Number}    rank    Unique of the mon within the cluster
  @apiSuccess {Boolean}   in_quorum      True if the mon is a member of current quorum
  @apiSuccess {String}    server        FQDN of server running the OSD
  @apiSuccess {String}    addr      IP address of monitor service

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "election_epoch": 77,
        "state": "leader",
        "monmap": {
          "quorum": [
            0,
            1,
            2
          ],
          "created": "2014-11-06T15:14:34.316557",
          "modified": "2014-11-06T15:14:34.316541",
          "epoch": 0,
          "mons": [
            {
              "name": "figment000",
              "rank": 0,
              "addr": ""
            },
            {
              "name": "figment001",
              "rank": 1,
              "addr": ""
            },
            {
              "name": "figment002",
              "rank": 2,
              "addr": ""
            }
          ],
          "fsid": "dce20d46-f010-4883-988c-4a6d8bd15793"
        },
        "rank": 0,
        "quorum": [
          0,
          1,
          2
        ]
      }
"""
def getMonStatus(){return;}


"""
  @api {get} /cluster/${uuid}/pool List Pools
  @apiName Pools
  @apiVersion 0.1.0
  @apiGroup pool
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {String}    name    Human readable name of the pool
  @apiSuccess {String}    id      Unique numeric ID
  @apiSuccess {Number}    size    Replication factor
  @apiSuccess {Number}    pg_num      Number of placement groups in this pool
  @apiSuccess {Number}    crush_ruleset     CRUSH ruleset in use
  @apiSuccess {Number}    min_size      Minimum number of replicas required for I/O
  @apiSuccess {Number}    crash_replay_interval   Number of seconds to allow clients to replay acknowledged
  @apiSuccess {Number}    pgp_num      Effective number of placement groups to use when calculating data placement
  @apiSuccess {Boolean}   hashpspool   Enable HASHPSPOOL flag
  @apiSuccess {Boolean}   full      True if the pool is full
  @apiSuccess {Number}    quota_max_objects      Quota limit on object count (0 is unlimited)
  @apiSuccess {Number}    quota_max_bytes        Quota limit on usage in bytes (0 is unlimited)

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          "full": false,
          "name": "data",
          "quota_max_objects": 0,
          "hashpspool": false,
          "min_size": 1,
          "crash_replay_interval": 0,
          "pg_num": 64,
          "pgp_num": 64,
          "quota_max_bytes": 0,
          "size": 2,
          "id": 0,
          "crush_ruleset": 2
        },
        {
          "full": false,
          "name": "metadata",
          "quota_max_objects": 0,
          "hashpspool": false,
          "min_size": 1,
          "crash_replay_interval": 0,
          "pg_num": 64,
          "pgp_num": 64,
          "quota_max_bytes": 0,
          "size": 2,
          "id": 1,
          "crush_ruleset": 2
        },
        {
          "full": false,
          "name": "rbd",
          "quota_max_objects": 0,
          "hashpspool": false,
          "min_size": 1,
          "crash_replay_interval": 0,
          "pg_num": 64,
          "pgp_num": 64,
          "quota_max_bytes": 0,
          "size": 2,
          "id": 2,
          "crush_ruleset": 2
        },
        {
          "full": false,
          "name": "newname",
          "quota_max_objects": 0,
          "hashpspool": false,
          "min_size": 1,
          "crash_replay_interval": 0,
          "pg_num": 64,
          "pgp_num": 64,
          "quota_max_bytes": 0,
          "size": 2,
          "id": 3,
          "crush_ruleset": 2
        }
      ]
"""
def Pools(){return;}

"""
  @api {post} /cluster/${uuid}/pool Create Pools
  @apiName CreatePool
  @apiVersion 0.1.0
  @apiGroup pool
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "full": false,
        "name": "data",
        "quota_max_objects": 0,
        "hashpspool": false,
        "min_size": 1,
        "crash_replay_interval": 0,
        "pg_num": 64,
        "pgp_num": 64,
        "quota_max_bytes": 0,
        "size": 2,
        "id": 0,
        "crush_ruleset": 2
      }
"""
def CreatePool(){return;}

"""
  @api {delete} /cluster/${uuid}/pool/{pool_id} Delete Pools
  @apiName deletePool
  @apiVersion 0.1.0
  @apiGroup pool
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID 

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
      }
"""
def DeletePool(){return;}


"""
  @api {patch} /cluster/${uuid}/pool/{pool_id}/ Update Pool Metadatas
  @apiName updatePool
  @apiVersion 0.1.0
  @apiGroup pool
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        key: min_size
        value: 3
      }
"""
def updatePool(){return;}

"""
  @api {get} /cluster/${uuid}/pool/{pool_id} Get Pool
  @apiName getPool
  @apiVersion 0.1.0
  @apiGroup pool
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID

  @apiSuccess {String}    name    Human readable name of the pool
  @apiSuccess {String}    id      Unique numeric ID
  @apiSuccess {Number}    size    Replication factor
  @apiSuccess {Number}    pg_num      Number of placement groups in this pool
  @apiSuccess {Number}    crush_ruleset     CRUSH ruleset in use
  @apiSuccess {Number}    min_size      Minimum number of replicas required for I/O
  @apiSuccess {Number}    crash_replay_interval   Number of seconds to allow clients to replay acknowledged
  @apiSuccess {Number}    pgp_num      Effective number of placement groups to use when calculating data placement
  @apiSuccess {Boolean}   hashpspool   Enable HASHPSPOOL flag
  @apiSuccess {Boolean}   full      True if the pool is full
  @apiSuccess {Number}    quota_max_objects      Quota limit on object count (0 is unlimited)
  @apiSuccess {Number}    quota_max_bytes        Quota limit on usage in bytes (0 is unlimited)

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "full": false,
        "name": "data",
        "quota_max_objects": 0,
        "hashpspool": false,
        "min_size": 1,
        "crash_replay_interval": 0,
        "pg_num": 64,
        "pgp_num": 64,
        "quota_max_bytes": 0,
        "size": 2,
        "id": 0,
        "crush_ruleset": 2
      }

"""
def getPool(){return;}

"""
  @api {get} /cluster/${uuid}/osd List OSDs
  @apiName Osd
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {String}    uuid    Globally unique ID for this OSD
  @apiSuccess {Boolean}   up      Whether the OSD is running from the point of view of the rest of the cluster
  @apiSuccess {Boolean}   in      Whether the OSD is ‘in’ the set of OSDs which will be used to store data
  @apiSuccess {Number}    id      ID of this OSD within this cluster
  @apiSuccess {Number}    reweight  CRUSH weight factor
  @apiSuccess {String}    server  FQDN of server this OSD was last running on   
  @apiSuccess {Object}    pools   List of pool IDs which use this OSD for storage
  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD
  @apiSuccess {String}    public_addr        Public/frontend IP address
  @apiSuccess {String}    cluster_addr       Cluster/backend IP address

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          "uuid": "9b2e324f-109d-449e-af60-f5f0b8fa5af0",
          "reweight": 1.0,
          "up": true,
          "server": "figment000.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 0
        },
        {
          "uuid": "065fb1d7-4a50-4141-a091-ae4551b6c381",
          "reweight": 1.0,
          "up": true,
          "server": "figment000.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 1
        },
        {
          "uuid": "426dcd12-fc70-4e1b-b9e0-4ad49ef21673",
          "reweight": 1.0,
          "up": true,
          "server": "figment000.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 2
        },
        {
          "uuid": "863f6f4b-99da-413f-b7c1-a68b9deeef9f",
          "reweight": 1.0,
          "up": true,
          "server": "figment000.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 3
        },
        {
          "uuid": "55d6e022-56e6-46ce-b336-255d3d34b184",
          "reweight": 1.0,
          "up": true,
          "server": "figment001.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 4
        },
        {
          "uuid": "275861f9-dd1f-4bd0-a36a-1143c0878895",
          "reweight": 1.0,
          "up": true,
          "server": "figment001.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 5
        },
        {
          "uuid": "2c86f528-ffff-44ed-a190-de649946a6e7",
          "reweight": 1.0,
          "up": true,
          "server": "figment001.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 6
        },
        {
          "uuid": "ff9deff7-b352-4f78-acd6-80e8fac40faa",
          "reweight": 1.0,
          "up": true,
          "server": "figment001.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 7
        },
        {
          "uuid": "fb8e2720-815c-4343-ae7e-4ffd33158926",
          "reweight": 1.0,
          "up": true,
          "server": "figment002.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 8
        },
        {
          "uuid": "7fa61048-93a8-436f-aa81-bba0e6d446dc",
          "reweight": 1.0,
          "up": true,
          "server": "figment002.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 9
        },
        {
          "uuid": "c019af21-368b-415b-ac94-b8d46cbb095d",
          "reweight": 1.0,
          "up": true,
          "server": "figment002.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 10
        },
        {
          "uuid": "a601c5fb-eae4-4565-abce-d14c45dba37d",
          "reweight": 1.0,
          "up": true,
          "server": "figment002.cluster0.com",
          "public_addr": "",
          "in": true,
          "pools": [
            0,
            1,
            2,
            3
          ],
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ],
          "cluster_addr": "",
          "id": 11
        }
      ]
"""
def Osd(){return;}

"""
  @api {post} /cluster/${uuid}/osd Create OSD
  @apiName CreateOsd
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {String}    uuid    Globally unique ID for this OSD
  @apiSuccess {Boolean}   up      Whether the OSD is running from the point of view of the rest of the cluster
  @apiSuccess {Boolean}   in      Whether the OSD is ‘in’ the set of OSDs which will be used to store data
  @apiSuccess {Number}    id      ID of this OSD within this cluster
  @apiSuccess {Number}    reweight  CRUSH weight factor
  @apiSuccess {String}    server  FQDN of server this OSD was last running on
  @apiSuccess {Object}    pools   List of pool IDs which use this OSD for storage
  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD
  @apiSuccess {String}    public_addr        Public/frontend IP address
  @apiSuccess {String}    cluster_addr       Cluster/backend IP address

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {}
"""
def CreateOsd(){return;}

"""
  @api {delete} /cluster/${uuid}/osd/${osd_id} Delete OSD
  @apiName DeleteOsd
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id OSD ID

  @apiSuccess {String}    uuid    Globally unique ID for this OSD
  @apiSuccess {Boolean}   up      Whether the OSD is running from the point of view of the rest of the cluster
  @apiSuccess {Boolean}   in      Whether the OSD is ‘in’ the set of OSDs which will be used to store data
  @apiSuccess {Number}    id      ID of this OSD within this cluster
  @apiSuccess {Number}    reweight  CRUSH weight factor
  @apiSuccess {String}    server  FQDN of server this OSD was last running on
  @apiSuccess {Object}    pools   List of pool IDs which use this OSD for storage
  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD
  @apiSuccess {String}    public_addr        Public/frontend IP address
  @apiSuccess {String}    cluster_addr       Cluster/backend IP address

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {}
"""
def DeleteOsd(){return;}

"""
  @api {get} /cluster/${uuid}/osd/${osd_id} Get OSD
  @apiName getOsd
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id ID of OSD

  @apiSuccess {String}    uuid    Globally unique ID for this OSD
  @apiSuccess {Boolean}   up      Whether the OSD is running from the point of view of the rest of the cluster
  @apiSuccess {Boolean}   in      Whether the OSD is ‘in’ the set of OSDs which will be used to store data
  @apiSuccess {Number}    id      ID of this OSD within this cluster
  @apiSuccess {Number}    reweight  CRUSH weight factor
  @apiSuccess {String}    server  FQDN of server this OSD was last running on
  @apiSuccess {Object}    pools   List of pool IDs which use this OSD for storage
  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD
  @apiSuccess {String}    public_addr        Public/frontend IP address
  @apiSuccess {String}    cluster_addr       Cluster/backend IP address

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "uuid": "9b2e324f-109d-449e-af60-f5f0b8fa5af0",
        "reweight": 1.0,
        "up": true,
        "server": "figment000.cluster0.com",
        "public_addr": "",
        "in": true,
        "pools": [
          0,
          1,
          2,
          3
        ],
        "valid_commands": [
          "scrub",
          "deep_scrub",
          "repair"
        ],
        "cluster_addr": "",
        "id": 0
      }
"""
def getOsd(){return;}

"""
  @api {get} /cluster/${uuid}/osd/command Get support command of OSD
  @apiName OsdCommand
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        "scrub",
        "deep_scrub",
        "repair"
      ]
"""
def OsdCommand(){return;}

"""
  @api {get} /cluster/${uuid}/osd/${osd_id}/command Get Specific support command of specific OSD
  @apiName getOsdCommand
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id ID of OSD

  @apiSuccess {Number}    id      ID of this OSD within this cluster
  @apiSuccess {String}    valid_commands     List of commands that can be applied to this OSD

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "0": {
          "valid_commands": [
            "scrub",
            "deep_scrub",
            "repair"
          ]
        }
      }
"""
def getOsdCommand(){return;}

"""
  @api {get} /cluster/${uuid}/osd/${osd_id}/command/${command} validate command of a specific OSD
  @apiName validateOsdCommand
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {Number} id ID of OSD
  @apiParam {String} command Command to be validated

  @apiSuccess {Boolean}    valid    OSD support specific command

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "valid": true
      }
"""
def validateOsdCommand(){return;}

"""
  @api {get} /cluster/${uuid}/osd_status Manage flags in the OsdMap
  @apiName OsdFlag
  @apiVersion 0.1.0
  @apiGroup OSD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster

  @apiSuccess {Boolean}    pause         Disable IO requests to all OSDs in cluster
  @apiSuccess {Boolean}    noup          Prevent OSDs from automatically getting marked as Up by the monitors. This setting is useful for troubleshooting
  @apiSuccess {Boolean}    nodown        Prevent OSDs from automatically getting marked as Down by the monitors. This setting is useful for troubleshooting
  @apiSuccess {Boolean}    noout         Prevent Down OSDs from being marked as out
  @apiSuccess {Boolean}    noin          Prevent OSDs from booting OSDs from being marked as IN. Will cause cluster health to be set to WARNING
  @apiSuccess {Boolean}    nobackfill    Disable backfill operations on cluster
  @apiSuccess {Boolean}    norecover     Disable replication of Placement Groups
  @apiSuccess {Boolean}    noscrub       Disables automatic periodic scrub operations on OSDs. May still be initiated on demand
  @apiSuccess {Boolean}    nodeep-scrub  Disables automatic periodic deep scrub operations on OSDs. May still be initiated on demand

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "pause": false,
        "nobackfill": false,
        "noout": false,
        "nodeep-scrub": false,
        "noscrub": false,
        "noin": false,
        "noup": false,
        "norecover": false,
        "nodown": false
      }
"""
def OsdFlag(){return;}

"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd List Rbd
  @apiName Rbd
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID

  @apiSuccess {String}    name         Rbd Name

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        "test1\ntest2"
      ]
"""
def Rbd(){return;}

"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name} Get Rbd
  @apiName getRbd
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name Rbd Name

  @apiSuccess {String}    size        Rbd Size
  @apiSuccess {Number}    order       Rbd Order
  @apiSuccess {String}    prefix      Rbd Prefix
  @apiSuccess {Number}    format      Rbd Format
  @apiSuccess {String}    feature     Rbd feature bits
  @apiSuccess {String}    flag        Rbd flags
  @apiSuccess {String}    parent      Rbd parents
  @apiSuccess {String}    overlap     Rbd Overlap

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        size: 10240 kB 
        order: 22 
        prefix: rbd_data.37646b8b4567
        format: 2
        features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
        flags:
        parent: rbd/tes@snap
        overlap: 10240 kB
      }
"""
def getRbd(){return;}

"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/snap List Snapshot 
  @apiName RbdSnap
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name Rbd Name

  @apiSuccess {String}    name        Snapshot Name
  @apiSuccess {Number}    snapid          Snapshot ID
  @apiSuccess {String}    size        Snapshot Size

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          name: snap
          snapid: 4
          size: 10240 kB
        },
      ]
"""
def getRbd(){return;}


"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/lock List Locks
  @apiName RbdLock
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name Rbd Name

  @apiSuccess {List}    lockers       Lockers' Name
  @apiSuccess {Boolean}   exclusive   wheth it is exclusive lock
  @apiSuccess {String}    tag         lock tags

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        lockers: [(u'client.1084750', u'test-lock', u'10.21.1.12:0/3412829308')]
        exclusive: True
        tag: ''
      }
"""
def getRbdLock(){return;}

"""
  @api {delete} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/lock/${lock_name} Remove Locks
  @apiName RbdLock
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name Rbd Name
  @apiParam {String} lock_name Lock Name

  @apiSuccess {String}    lock_name         Lock Name

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        lcok_name: 'test_lock'
      }
"""
def deleteRbdLock(){return;}

"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/snap/${snap_name}/ Get Children of Snapshot
  @apiName RbdSnapChildren
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name Rbd Name
  @apiParam {String} snap_name Snap Name

  @apiSuccess {String}    pool         Pool Name
  @apiSuccess {String}    name         Rbd Name

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          pool: 'rbd'
          name: 'clone'
        },
      ]
"""
def getRbdSnapChildren(){return;}

"""
  @api {get} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/meta List Rbd Meta
  @apiName RbdMeta
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name RBD Name

  @apiSuccess {String}    key        Config Key
  @apiSuccess {String}    value      Config Value

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          'key': rbd_cache
          'value': false
        },
      ]
"""
def RbdMeta(){return;}

"""
  @api {post} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/meta/${key} Set Rbd Meta
  @apiName setRbdMeta
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name RBD Name
  @apiParam {String} key Config Key

  @apiSuccess {String}    key        Config Key
  @apiSuccess {String}    value      Config Value

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          'key': rbd_cache
          'value': false
        },
      ]
"""
def setRbdMeta(){return;}

"""
  @api {delete} /cluster/${uuid}/pool/${pool_id}/rbd/${rbd_name}/meta/${key} Delete Rbd Meta
  @apiName deleteRbdMeta
  @apiVersion 0.1.0
  @apiGroup RBD
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} pool_id Pool ID
  @apiParam {String} rbd_name RBD Name
  @apiParam {String} key Config Key 

  @apiSuccess {String}    key        Config Key

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          'key': rbd_cache
        },
      ]
"""
def deleteRbdMeta(){return;}

"""
  @api {get} /cluster/${uuid}/config/${key} Get a Configuration Option
  @apiName getClusterConfig
  @apiVersion 0.1.0
  @apiGroup Config
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} key Config Key
 
  @apiSuccess {String}    value    Config Value
  @apiSuccess {String}    key      Config Key
 
  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "value": "10",
        "key": "mds_bal_interval"
      }
"""
def getClusterConfig(){return;}

"""
  @api {post} /cluster/${uuid}/config/${key} Update a Configuration Option
  @apiName updateClusterConfig
  @apiVersion 0.1.0
  @apiGroup Config
  @apiPermission admin

  @apiParam {String} uuid UUID of Cluster
  @apiParam {String} key Config Key

  @apiSuccess {String}    value    Config Value
  @apiSuccess {String}    key      Config Key

  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      {
        "value": "10",
        "key": "mds_bal_interval"
      }
"""
def updateClusterConfig(){return;}


"""
  @api {get} /cluster/${uuid}/config List Configuration 
  @apiName ClusterConfig
  @apiVersion 0.1.0
  @apiGroup Config
  @apiPermission admin
 
  @apiParam {String} uuid UUID of Cluster
 
  @apiSuccess {String}    value    Config Value
  @apiSuccess {String}    key      Config Key
 
  @apiSuccessExample {json} SuccessReponse:
      HTTP/1.1 200 OK
      [
        {
          "value": "43200",
          "key": "auth_mon_ticket_ttl"
        },
        {
          "value": "0",
          "key": "journal_replay_from"
        },
        {
          "value": "1",
          "key": "ms_inject_delay_max"
        },
        {
          "value": "",
          "key": "rgw_swift_auth_url"
        },
        {
          "value": "1/5",
          "key": "mds_log_expire"
        },
        {
          "value": "false",
          "key": "osd_debug_pg_log_writeout"
        },
        {
          "value": "500",
          "key": "filestore_wbthrottle_xfs_inodes_start_flusher"
        },
        {
          "value": "1",
          "key": "rbd_default_stripe_count"
        },
        {
          "value": "0.3",
          "key": "mon_osd_laggy_weight"
        },
        {
          "value": "500",
          "key": "mon_max_pgmap_epochs"
        },
        {
          "value": "0/5",
          "key": "osd"
        },
        {
          "value": "10",
          "key": "mon_accept_timeout"
        },
        {
          "value": "419430400",
          "key": "mon_daemon_bytes"
        },
        {
          "value": "16384",
          "key": "client_cache_size"
        },
        {
          "value": "10",
          "key": "rbd_concurrent_management_ops"
        },
        {
          "value": "false",
          "key": "osd_use_stale_snap"
        },
        {
          "value": "0/5",
          "key": "tp"
        },
        {
          "value": "cephx",
          "key": "auth_client_required"
        },
        {
          "value": "3600",
          "key": "rgw_gc_processor_max_time"
        },
        {
          "value": "4",
          "key": "client_readahead_max_periods"
        },
        {
          "value": "2",
          "key": "mon_probe_timeout"
        },
        {
          "value": "256",
          "key": "osd_command_max_records"
        },
        {
          "value": "3600",
          "key": "mon_osd_laggy_halflife"
        },
        {
          "value": "",
          "key": "rgw_keystone_admin_token"
        },
        {
          "value": "10",
          "key": "osd_recover_clone_overlap_limit"
        },
        {
          "value": "5",
          "key": "client_oc_max_dirty_age"
        },
        {
          "value": "swift",
          "key": "rgw_swift_url_prefix"
        },
        {
          "value": "/var/log/ceph/myceph-mon.gravel1.tdump",
          "key": "mon_debug_dump_location"
        },
        {
          "value": "false",
          "key": "cephx_service_require_signatures"
        },
        {
          "value": "300",
          "key": "mon_subscribe_interval"
        },
        {
          "value": "10",
          "key": "paxos_max_join_drift"
        },
        {
          "value": "7200",
          "key": "rgw_gc_obj_min_wait"
        },
        {
          "value": "0",
          "key": "mds_kill_journal_replay_at"
        },
        {
          "value": "1/5",
          "key": "mds_locker"
        },
        {
          "value": "false",
          "key": "filestore_debug_inject_read_err"
        },
        {
          "value": "10000",
          "key": "mds_bal_split_wr"
        },
        {
          "value": "104857600",
          "key": "filestore_queue_max_bytes"
        },
        {
          "value": "%Y-%m-%d-%H-%i-%n",
          "key": "rgw_log_object_name"
        },
        {
          "value": "0.8",
          "key": "osd_age"
        },
        {
          "value": "192.168.18.0/24",
          "key": "public_network"
        },
        {
          "value": "45",
          "key": "osd_default_data_pool_replay_window"
        },
        {
          "value": "0",
          "key": "osd_pool_default_min_size"
        },
        {
          "value": "1000",
          "key": "filestore_update_to"
        },
        {
          "value": "1.2",
          "key": "mds_bal_need_max"
        },
        {
          "value": "true",
          "key": "osd_leveldb_compression"
        },
        {
          "value": "1048576",
          "key": "mds_mem_max"
        },
        {
          "value": "5000",
          "key": "filestore_wbthrottle_btrfs_ios_hard_limit"
        },
        {
          "value": "1024",
          "key": "osd_max_pgls"
        },
        {
          "value": "0/1",
          "key": "context"
        },
        {
          "value": "false",
          "key": "filestore_fsync_flushes_journal_data"
        },
        {
          "value": "0/5",
          "key": "objectcacher"
        },
        {
          "value": "10",
          "key": "osd_recovery_op_priority"
        },
        {
          "value": "false",
          "key": "mds_dump_cache_after_rejoin"
        },
        {
          "value": "41943040",
          "key": "filestore_wbthrottle_btrfs_bytes_start_flusher"
        },
        {
          "value": "0.05",
          "key": "mon_clock_drift_allowed"
        },
        {
          "value": "300",
          "key": "rgw_init_timeout"
        },
        {
          "value": "false",
          "key": "osd_verify_sparse_read_holes"
        },
        {
          "value": "1",
          "key": "mds_replay_interval"
        },
        {
          "value": "0",
          "key": "mon_leveldb_max_open_files"
        },
        {
          "value": "1",
          "key": "osd_max_scrubs"
        },
        {
          "value": "0",
          "key": "mds_kill_journal_at"
        },
        {
          "value": "0",
          "key": "osd_leveldb_max_open_files"
        },
        {
          "value": "false",
          "key": "log_to_syslog"
        },
        {
          "value": "true",
          "key": "mon_compact_on_trim"
        },
        {
          "value": "false",
          "key": "osd_debug_verify_snaps_on_info"
        },
        {
          "value": "false",
          "key": "filestore_blackhole"
        },
        {
          "value": "0",
          "key": "paxos_kill_at"
        },
        {
          "value": "10",
          "key": "osd_max_push_objects"
        },
        {
          "value": "%Y-%m-%d-%i-%n",
          "key": "rgw_intent_log_object_name"
        },
        {
          "value": ":/0",
          "key": "osd_heartbeat_addr"
        },
        {
          "value": "300",
          "key": "mon_osd_down_out_interval"
        },
        {
          "value": "600",
          "key": "rgw_bucket_quota_ttl"
        },
        {
          "value": "true",
          "key": "fatal_signal_handlers"
        },
        {
          "value": "1000",
          "key": "mds_bal_merge_wr"
        },
        {
          "value": "6",
          "key": "osd_pg_bits"
        },
        {
          "value": "500",
          "key": "paxos_service_trim_max"
        },
        {
          "value": "3600",
          "key": "rgw_gc_processor_period"
        },
        {
          "value": "30",
          "key": "mon_pg_create_interval"
        },
        {
          "value": "false",
          "key": "filestore_debug_omap_check"
        },
        {
          "value": "true",
          "key": "rgw_ops_log_rados"
        },
        {
          "value": "20",
          "key": "osd_op_history_size"
        },
        {
          "value": "0",
          "key": "mds_kill_journal_expire_at"
        },
        {
          "value": "false",
          "key": "daemonize"
        },
        {
          "value": "1",
          "key": "rbd_default_format"
        },
        {
          "value": "0",
          "key": "osd_age_time"
        },
        {
          "value": "10000",
          "key": "rgw_keystone_token_cache_size"
        },
        {
          "value": "0.001",
          "key": "mds_bal_minchunk"
        },
        {
          "value": "5000",
          "key": "filestore_wbthrottle_xfs_inodes_hard_limit"
        },
        {
          "value": "2",
          "key": "filestore_split_multiple"
        },
        {
          "value": "/etc/mime.types",
          "key": "rgw_mime_types_file"
        },
        {
          "value": "1",
          "key": "osd_disk_threads"
        },
        {
          "value": "0.85",
          "key": "mon_osd_nearfull_ratio"
        },
        {
          "value": "1024",
          "key": "objecter_inflight_ops"
        },
        {
          "value": "5",
          "key": "osd_mon_shutdown_timeout"
        },
        {
          "value": "5242880",
          "key": "rgw_ops_log_data_backlog"
        },
        {
          "value": "true",
          "key": "perf"
        },
        {
          "value": "2048",
          "key": "filestore_max_inline_xattr_size_btrfs"
        },
        {
          "value": "false",
          "key": "osd_check_for_log_corruption"
        },
        {
          "value": "false",
          "key": "osd_auto_weight"
        },
        {
          "value": "Member, admin",
          "key": "rgw_keystone_accepted_roles"
        },
        {
          "value": "300",
          "key": "journal_queue_max_ops"
        },
        {
          "value": "",
          "key": "pid_file"
        },
        {
          "value": "1000",
          "key": "osd_push_per_object_cost"
        },
        {
          "value": "1",
          "key": "max_mds"
        },
        {
          "value": "false",
          "key": "cephx_cluster_require_signatures"
        },
        {
          "value": "true",
          "key": "rgw_s3_auth_use_rados"
        },
        {
          "value": "false",
          "key": "ms_nocrc"
        },
        {
          "value": "65536",
          "key": "mon_max_pool_pg_num"
        },
        {
          "value": "info",
          "key": "mon_cluster_log_file_level"
        },
        {
          "value": "0",
          "key": "mds_kill_export_at"
        },
        {
          "value": "1",
          "key": "rbd_cache_max_dirty_age"
        },
        {
          "value": "0",
          "key": "mds_inject_traceless_reply_probability"
        },
        {
          "value": "0/5",
          "key": "none"
        },
        {
          "value": "/",
          "key": "chdir"
        },
        {
          "value": "0",
          "key": "mds_kill_mdstable_at"
        },
        {
          "value": "0",
          "key": "mon_leveldb_bloom_size"
        },
        {
          "value": "",
          "key": "rgw_dns_name"
        },
        {
          "value": "8",
          "key": "osd_pool_default_pg_num"
        },
        {
          "value": "0/5",
          "key": "rados"
        },
        {
          "value": "0/5",
          "key": "ms"
        },
        {
          "value": "/var/lib/ceph/mon/myceph-gravel1",
          "key": "mon_data"
        },
        {
          "value": "false",
          "key": "filestore_journal_parallel"
        },
        {
          "value": "10",
          "key": "journaler_prefetch_periods"
        },
        {
          "value": "0",
          "key": "clock_offset"
        },
        {
          "value": "30",
          "key": "mon_data_avail_warn"
        },
        {
          "value": "true",
          "key": "fuse_big_writes"
        },
        {
          "value": "false",
          "key": "inject_early_sigterm"
        },
        {
          "value": "512",
          "key": "osd_backfill_scan_max"
        },
        {
          "value": "false",
          "key": "rgw_log_object_name_utc"
        },
        {
          "value": "10485760",
          "key": "journal_max_corrupt_search"
        },
        {
          "value": "5000",
          "key": "filestore_wbthrottle_btrfs_inodes_hard_limit"
        },
        {
          "value": "5000",
          "key": "filestore_wbthrottle_xfs_ios_hard_limit"
        },
        {
          "value": "0",
          "key": "heartbeat_inject_failure"
        },
        {
          "value": "0",
          "key": "mon_pool_quota_warn_threshold"
        },
        {
          "value": "-1",
          "key": "mds_bal_max_until"
        },
        {
          "value": "10",
          "key": "mon_lease_ack_timeout"
        },
        {
          "value": "1048576",
          "key": "ms_rwthread_stack_bytes"
        },
        {
          "value": "65536",
          "key": "osd_op_pq_min_cost"
        },
        {
          "value": "true",
          "key": "mds_early_reply"
        },
        {
          "value": "0/5",
          "key": "journaler"
        },
        {
          "value": "/var/lib/ceph/radosgw/myceph-gravel1",
          "key": "rgw_data"
        },
        {
          "value": "-1",
          "key": "mon_sync_debug_provider_fallback"
        },
        {
          "value": "500",
          "key": "paxos_min"
        },
        {
          "value": "536870912",
          "key": "mon_leveldb_cache_size"
        },
        {
          "value": "false",
          "key": "filestore"
        },
        {
          "value": "8388608",
          "key": "osd_max_push_cost"
        },
        {
          "value": "100",
          "key": "osd_scan_list_ping_tp_interval"
        },
        {
          "value": "/var/lib/ceph/osd/myceph-gravel1/journal",
          "key": "osd_journal"
        },
        {
          "value": "false",
          "key": "journal_zero_on_create"
        },
        {
          "value": "4194304",
          "key": "osd_op_pq_max_tokens_per_priority"
        },
        {
          "value": "1",
          "key": "mds_dirstat_min_interval"
        },
        {
          "value": "4096",
          "key": "filestore_fiemap_threshold"
        },
        {
          "value": "0",
          "key": "osd_debug_drop_ping_probability"
        },
        {
          "value": "",
          "key": "keyfile"
        },
        {
          "value": "0",
          "key": "osd_debug_drop_pg_create_probability"
        },
        {
          "value": "0.97",
          "key": "log_stop_at_utilization"
        },
        {
          "value": "true",
          "key": "journaler_allow_split_entries"
        },
        {
          "value": "604800",
          "key": "osd_scrub_max_interval"
        },
        {
          "value": "cephx",
          "key": "auth_cluster_required"
        },
        {
          "value": "0",
          "key": "osd_leveldb_bloom_size"
        },
        {
          "value": "true",
          "key": "fuse_atomic_o_trunc"
        },
        {
          "value": "0",
          "key": "mon_pool_quota_crit_threshold"
        },
        {
          "value": "daemon",
          "key": "clog_to_syslog_facility"
        },
        {
          "value": "5",
          "key": "osd_mon_report_interval_min"
        },
        {
          "value": "0",
          "key": "filestore_max_inline_xattr_size"
        },
        {
          "value": "rack",
          "key": "mon_osd_down_out_subtree_limit"
        },
        {
          "value": "3",
          "key": "mon_osd_min_down_reports"
        },
        {
          "value": "false",
          "key": "mutex_perf_counter"
        },
        {
          "value": "60",
          "key": "mds_session_timeout"
        },
        {
          "value": "5",
          "key": "mon_clock_drift_warn_backoff"
        },
        {
          "value": "4096",
          "key": "mon_max_log_entries_per_event"
        },
        {
          "value": "1",
          "key": "mon_osd_min_down_reporters"
        },
        {
          "value": "true",
          "key": "mon_osd_adjust_down_out_interval"
        },
        {
          "value": "false",
          "key": "rgw_relaxed_s3_bucket_names"
        },
        {
          "value": "500",
          "key": "osd_pg_stat_report_interval_max"
        },
        {
          "value": "false",
          "key": "ms_die_on_bad_msg"
        },
        {
          "value": "0",
          "key": "ms_inject_internal_delays"
        },
        {
          "value": "50",
          "key": "mds_bal_merge_size"
        },
        {
          "value": "16777216",
          "key": "rgw_get_obj_window_size"
        },
        {
          "value": "false",
          "key": "osd_debug_op_order"
        },
        {
          "value": "1/5",
          "key": "auth"
        },
        {
          "value": "500",
          "key": "mon_max_log_epochs"
        },
        {
          "value": "900",
          "key": "mon_osd_report_timeout"
        },
        {
          "value": "true",
          "key": "filestore_wbthrottle_enable"
        },
        {
          "value": "30",
          "key": "osd_recovery_thread_timeout"
        },
        {
          "value": "0.7",
          "key": "mds_cache_mid"
        },
        {
          "value": "mon.gravel1",
          "key": "name"
        },
        {
          "value": "0",
          "key": "osd_kill_backfill_at"
        },
        {
          "value": "33554432",
          "key": "rbd_cache_size"
        },
        {
          "value": "1/5",
          "key": "crypto"
        },
        {
          "value": "1024",
          "key": "rgw_usage_log_flush_threshold"
        },
        {
          "value": "true",
          "key": "mon_osd_auto_mark_auto_out_in"
        },
        {
          "value": "100",
          "key": "journal_max_write_entries"
        },
        {
          "value": "65536",
          "key": "journal_align_min_size"
        },
        {
          "value": "5",
          "key": "mon_lease"
        },
        {
          "value": "",
          "key": "rgw_swift_url"
        },
        {
          "value": "0",
          "key": "filestore_kill_at"
        },
        {
          "value": "5",
          "key": "osd_scrub_chunk_min"
        },
        {
          "value": "30",
          "key": "rgw_data_log_window"
        },
        {
          "value": "1/5",
          "key": "mds"
        },
        {
          "value": "300",
          "key": "client_mount_timeout"
        },
        {
          "value": "false",
          "key": "mon_compact_on_start"
        },
        {
          "value": "false",
          "key": "mon_cluster_log_to_syslog"
        },
        {
          "value": "",
          "key": "rgw_keystone_url"
        },
        {
          "value": "1000",
          "key": "mon_client_max_log_entries_per_message"
        },
        {
          "value": "42949672960",
          "key": "mon_leveldb_size_warn"
        },
        {
          "value": "100",
          "key": "osd_client_message_cap"
        },
        {
          "value": "/var/log/ceph/myceph.log",
          "key": "mon_cluster_log_file"
        },
        {
          "value": "300",
          "key": "mon_pg_stuck_threshold"
        },
        {
          "value": "15",
          "key": "journaler_write_head_interval"
        },
        {
          "value": "false",
          "key": "mds_debug_auth_pins"
        },
        {
          "value": "10",
          "key": "objecter_timeout"
        },
        {
          "value": "0",
          "key": "mon_sync_provider_kill_at"
        },
        {
          "value": "true",
          "key": "filestore_replica_fadvise"
        },
        {
          "value": "/var/lib/ceph/osd/myceph-gravel1",
          "key": "osd_data"
        },
        {
          "value": "104857600",
          "key": "client_oc_max_dirty"
        },
        {
          "value": "",
          "key": "restapi_base_url"
        },
        {
          "value": "419430400",
          "key": "filestore_wbthrottle_xfs_bytes_hard_limit"
        },
        {
          "value": "false",
          "key": "auth_debug"
        },
        {
          "value": "true",
          "key": "osd_recover_clone_overlap"
        },
        {
          "value": "65536",
          "key": "filestore_sloppy_crc_block_size"
        },
        {
          "value": "0",
          "key": "filestore_max_inline_xattrs"
        },
        {
          "value": "0/1",
          "key": "timer"
        },
        {
          "value": "8",
          "key": "rgw_num_control_oids"
        },
        {
          "value": "true",
          "key": "osd_map_dedup"
        },
        {
          "value": "0.75",
          "key": "client_cache_mid"
        },
        {
          "value": "false",
          "key": "ms_die_on_unhandled_msg"
        },
        {
          "value": "120",
          "key": "rgw_exit_timeout_secs"
        },
        {
          "value": "/dev/null",
          "key": "mon_leveldb_log"
        },
        {
          "value": "100",
          "key": "osd_map_message_max"
        },
        {
          "value": "true",
          "key": "fuse_allow_other"
        },
        {
          "value": "10000",
          "key": "mon_pg_warn_min_objects"
        },
        {
          "value": "10000",
          "key": "log_max_recent"
        },
        {
          "value": "true",
          "key": "journal_aio"
        },
        {
          "value": "false",
          "key": "mon_compact_on_bootstrap"
        },
        {
          "value": "true",
          "key": "ms_tcp_nodelay"
        },
        {
          "value": "false",
          "key": "mds_wipe_sessions"
        },
        {
          "value": "0",
          "key": "journaler_batch_max"
        },
        {
          "value": "false",
          "key": "rgw_enable_usage_log"
        },
        {
          "value": "5",
          "key": "journaler_prezero_periods"
        },
        {
          "value": "2",
          "key": "filestore_op_threads"
        },
        {
          "value": "8000",
          "key": "mds_bal_replicate_threshold"
        },
        {
          "value": "0",
          "key": "osd_leveldb_write_buffer_size"
        },
        {
          "value": "0",
          "key": "rgw_s3_success_create_obj_status"
        },
        {
          "value": "0.001",
          "key": "journaler_batch_interval"
        },
        {
          "value": "30",
          "key": "osd_mon_ack_timeout"
        },
        {
          "value": "true",
          "key": "fuse_default_permissions"
        },
        {
          "value": "0",
          "key": "osd_debug_drop_op_probability"
        },
        {
          "value": "10",
          "key": "mon_pg_warn_max_object_skew"
        },
        {
          "value": "10",
          "key": "osd_max_backfills"
        },
        {
          "value": "30",
          "key": "rgw_usage_log_tick_interval"
        },
        {
          "value": "/var/run/ceph/myceph-mon.gravel1.asok",
          "key": "admin_socket"
        },
        {
          "value": "0",
          "key": "osd_debug_drop_ping_duration"
        },
        {
          "value": "false",
          "key": "journal_ignore_corruption"
        },
        {
          "value": "1/1",
          "key": "throttle"
        },
        {
          "value": "500",
          "key": "paxos_trim_max"
        },
        {
          "value": "false",
          "key": "mds_log_skip_corrupt_events"
        },
        {
          "value": "",
          "key": "rgw_host"
        },
        {
          "value": "0",
          "key": "ms_tcp_rcvbuf"
        },
        {
          "value": "5120",
          "key": "osd_journal_size"
        },
        {
          "value": "600",
          "key": "osd_op_history_duration"
        },
        {
          "value": "0",
          "key": "mds_bal_unreplicate_threshold"
        },
        {
          "value": "3600",
          "key": "osd_remove_thread_timeout"
        },
        {
          "value": "30",
          "key": "osd_default_notify_timeout"
        },
        {
          "value": "replica_log",
          "key": "rgw_replica_log_obj_prefix"
        },
        {
          "value": "4",
          "key": "mds_beacon_interval"
        },
        {
          "value": "600",
          "key": "rgw_op_thread_timeout"
        },
        {
          "value": "512",
          "key": "filestore_max_inline_xattr_size_other"
        },
        {
          "value": "0.2",
          "key": "ms_initial_backoff"
        },
        {
          "value": "0.01",
          "key": "filestore_min_sync_interval"
        },
        {
          "value": "/dev/null",
          "key": "osd_leveldb_log"
        },
        {
          "value": "true",
          "key": "internal_safe_to_start_threads"
        },
        {
          "value": "",
          "key": "rgw_socket_path"
        },
        {
          "value": "false",
          "key": "mds_verify_scatter"
        },
        {
          "value": "60",
          "key": "mon_health_data_update_interval"
        },
        {
          "value": "0",
          "key": "filestore_inject_stall"
        },
        {
          "value": "22",
          "key": "rbd_default_order"
        },
        {
          "value": "300",
          "key": "mds_session_autoclose"
        },
        {
          "value": "false",
          "key": "mon_debug_dump_transactions"
        },
        {
          "value": "250",
          "key": "paxos_trim_min"
        },
        {
          "value": "65536",
          "key": "filestore_max_inline_xattr_size_xfs"
        },
        {
          "value": "30",
          "key": "mds_log_max_segments"
        },
        {
          "value": "128",
          "key": "rgw_num_zone_opstate_shards"
        },
        {
          "value": "131072",
          "key": "client_readahead_min"
        },
        {
          "value": "15",
          "key": "osd_op_thread_timeout"
        },
        {
          "value": "200",
          "key": "osd_pg_epoch_persisted_max_stale"
        },
        {
          "value": "0/1",
          "key": "buffer"
        },
        {
          "value": "25",
          "key": "paxos_stash_full_interval"
        },
        {
          "value": "41943040",
          "key": "filestore_wbthrottle_xfs_bytes_start_flusher"
        },
        {
          "value": "600",
          "key": "osd_scrub_finalize_thread_timeout"
        },
        {
          "value": "8388608",
          "key": "client_oc_target_dirty"
        },
        {
          "value": "10",
          "key": "osd_max_rep"
        },
        {
          "value": "600",
          "key": "filestore_commit_timeout"
        },
        {
          "value": "5",
          "key": "mds_bal_fragment_interval"
        },
        {
          "value": "104857600",
          "key": "filestore_queue_committing_max_bytes"
        },
        {
          "value": "false",
          "key": "osd_preserve_trimmed_log"
        },
        {
          "value": "true",
          "key": "log_flush_on_exit"
        },
        {
          "value": "1",
          "key": "osd_min_rep"
        },
        {
          "value": "0.05",
          "key": "paxos_min_wait"
        },
        {
          "value": "1",
          "key": "num_client"
        },
        {
          "value": "false",
          "key": "rgw_log_nonexistent_bucket"
        },
        {
          "value": "/etc/ceph/myceph.mon.gravel1.keyring,/etc/ceph/myceph.keyring,/etc/ceph/keyring,/etc/ceph/keyring.bin",
          "key": "keyring"
        },
        {
          "value": "3600",
          "key": "osd_snap_trim_thread_timeout"
        },
        {
          "value": "false",
          "key": "filestore_sloppy_crc"
        },
        {
          "value": "500",
          "key": "filestore_wbthrottle_xfs_ios_start_flusher"
        },
        {
          "value": "1048576",
          "key": "mon_sync_max_payload_size"
        },
        {
          "value": "20",
          "key": "osd_peering_wq_batch_size"
        },
        {
          "value": "/var/log/ceph/myceph-mon.gravel1.log",
          "key": "log_file"
        },
        {
          "value": "104857600",
          "key": "mon_client_bytes"
        },
        {
          "value": "false",
          "key": "filestore_journal_writeahead"
        },
        {
          "value": "20",
          "key": "osd_heartbeat_grace"
        },
        {
          "value": "1000",
          "key": "mon_pg_warn_min_pool_objects"
        },
        {
          "value": "",
          "key": "rgw_extended_http_attrs"
        },
        {
          "value": "90",
          "key": "osd_max_write_size"
        },
        {
          "value": "1000",
          "key": "rgw_data_log_changes_size"
        },
        {
          "value": "0",
          "key": "mon_inject_sync_get_chunk_delay"
        },
        {
          "value": "",
          "key": "client_trace"
        },
        {
          "value": "true",
          "key": "filestore_btrfs_snap"
        },
        {
          "value": "6",
          "key": "osd_heartbeat_interval"
        },
        {
          "value": ":/0",
          "key": "cluster_addr"
        },
        {
          "value": "1000",
          "key": "rgw_list_buckets_max_chunk"
        },
        {
          "value": "1/1",
          "key": "crush"
        },
        {
          "value": "0",
          "key": "max_open_files"
        },
        {
          "value": "-1",
          "key": "mds_log_max_events"
        },
        {
          "value": "5",
          "key": "objecter_tick_interval"
        },
        {
          "value": "1/5",
          "key": "mds_migrator"
        },
        {
          "value": "0/5",
          "key": "objclass"
        },
        {
          "value": "admin",
          "key": "rgw_admin_entry"
        },
        {
          "value": "20",
          "key": "mon_pg_warn_min_per_osd"
        },
        {
          "value": "3000",
          "key": "osd_min_pg_log_entries"
        },
        {
          "value": "128",
          "key": "filestore_fd_cache_size"
        },
        {
          "value": "false",
          "key": "mds_bal_frag"
        },
        {
          "value": "0.95",
          "key": "rgw_bucket_quota_soft_threshold"
        },
        {
          "value": "false",
          "key": "osd_compact_leveldb_on_mount"
        },
        {
          "value": "0/1",
          "key": "striper"
        },
        {
          "value": "500",
          "key": "mon_min_osdmap_epochs"
        },
        {
          "value": "5",
          "key": "mon_data_avail_crit"
        },
        {
          "value": "10",
          "key": "filestore_merge_threshold"
        },
        {
          "value": "0",
          "key": "mds_bal_mode"
        },
        {
          "value": "4096",
          "key": "mon_config_key_max_entry_size"
        },
        {
          "value": "0.3",
          "key": "mds_bal_midchunk"
        },
        {
          "value": "32",
          "key": "mon_osd_max_op_age"
        },
        {
          "value": "false",
          "key": "mon_leveldb_paranoid"
        },
        {
          "value": "5",
          "key": "mds_decay_halflife"
        },
        {
          "value": "0.9",
          "key": "osd_failsafe_nearfull_ratio"
        },
        {
          "value": "10000",
          "key": "mon_max_osd"
        },
        {
          "value": "false",
          "key": "osd_debug_verify_stray_on_activate"
        },
        {
          "value": ".rgw.root",
          "key": "rgw_region_root_pool"
        },
        {
          "value": "300",
          "key": "mon_timecheck_interval"
        },
        {
          "value": "25000",
          "key": "mds_bal_split_rd"
        },
        {
          "value": "0.5",
          "key": "osd_scrub_load_threshold"
        },
        {
          "value": "10000",
          "key": "rgw_bucket_quota_cache_size"
        },
        {
          "value": "10000",
          "key": "osd_max_pg_log_entries"
        },
        {
          "value": "262144",
          "key": "mon_slurp_bytes"
        },
        {
          "value": "1/5",
          "key": "javaclient"
        },
        {
          "value": "86400",
          "key": "rgw_swift_token_expiration"
        },
        {
          "value": "104857600",
          "key": "objecter_inflight_op_bytes"
        },
        {
          "value": "true",
          "key": "client_oc"
        },
        {
          "value": "60",
          "key": "filestore_op_thread_timeout"
        },
        {
          "value": "false",
          "key": "log_to_stderr"
        },
        {
          "value": "32",
          "key": "rgw_usage_max_shards"
        },
        {
          "value": "524288",
          "key": "osd_deep_scrub_stride"
        },
        {
          "value": "0",
          "key": "mon_osd_force_trim_to"
        },
        {
          "value": "10485760",
          "key": "journal_max_write_bytes"
        },
        {
          "value": "true",
          "key": "mds_enforce_unique_name"
        },
        {
          "value": ".snap",
          "key": "client_snapdir"
        },
        {
          "value": "false",
          "key": "filestore_journal_trailing"
        },
        {
          "value": "15",
          "key": "mds_beacon_grace"
        },
        {
          "value": "false",
          "key": "client_debug_force_sync_read"
        },
        {
          "value": "7300",
          "key": "ms_bind_port_max"
        },
        {
          "value": "0",
          "key": "client_debug_inject_tick_delay"
        },
        {
          "value": "3",
          "key": "mds_bal_split_bits"
        },
        {
          "value": "false",
          "key": "cephx_require_signatures"
        },
        {
          "value": "false",
          "key": "client_use_random_mds"
        },
        {
          "value": "",
          "key": "key"
        },
        {
          "value": "",
          "key": "rgw_zone"
        },
        {
          "value": "-1",
          "key": "mon_sync_debug_provider"
        },
        {
          "value": "/var/run/ceph",
          "key": "run_dir"
        },
        {
          "value": "120",
          "key": "osd_mon_report_interval_max"
        },
        {
          "value": "0/10",
          "key": "monc"
        },
        {
          "value": "1",
          "key": "osd_recovery_threads"
        },
        {
          "value": "true",
          "key": "journal_block_align"
        },
        {
          "value": "false",
          "key": "lockdep"
        },
        {
          "value": "0",
          "key": "osd_max_attr_size"
        },
        {
          "value": "0",
          "key": "mds_open_remote_link_mode"
        },
        {
          "value": "192.168.19.0/24",
          "key": "cluster_network"
        },
        {
          "value": "1/5",
          "key": "paxos"
        },
        {
          "value": "33554432",
          "key": "journal_queue_max_bytes"
        },
        {
          "value": "16",
          "key": "osd_recovery_op_warn_multiple"
        },
        {
          "value": "false",
          "key": "rgw_s3_auth_use_keystone"
        },
        {
          "value": "",
          "key": "rgw_port"
        },
        {
          "value": "0",
          "key": "osd_leveldb_cache_size"
        },
        {
          "value": "0",
          "key": "ms_inject_delay_probability"
        },
        {
          "value": ":/0",
          "key": "public_addr"
        },
        {
          "value": "false",
          "key": "mds_dump_cache_on_map"
        },
        {
          "value": "900",
          "key": "ms_tcp_read_timeout"
        },
        {
          "value": "65536",
          "key": "mon_leveldb_block_size"
        },
        {
          "value": "0",
          "key": "mds_kill_rename_at"
        },
        {
          "value": "0",
          "key": "mds_kill_import_at"
        },
        {
          "value": "false",
          "key": "osd_recovery_forget_lost_objects"
        },
        {
          "value": "30",
          "key": "osd_target_transaction_size"
        },
        {
          "value": "daemon",
          "key": "mon_cluster_log_to_syslog_facility"
        },
        {
          "value": "2",
          "key": "mon_stat_smooth_intervals"
        },
        {
          "value": "false",
          "key": "mds_debug_subtrees"
        },
        {
          "value": "true",
          "key": "rgw_print_continue"
        },
        {
          "value": "true",
          "key": "mon_force_standby_active"
        },
        {
          "value": "default.region",
          "key": "rgw_default_region_info_oid"
        },
        {
          "value": "5",
          "key": "mon_sync_fs_threshold"
        },
        {
          "value": "true",
          "key": "mon_osd_auto_mark_new_in"
        },
        {
          "value": "/",
          "key": "client_mountpoint"
        },
        {
          "value": "1/1",
          "key": "finisher"
        },
        {
          "value": "data_log",
          "key": "rgw_data_log_obj_prefix"
        },
        {
          "value": "1/5",
          "key": "mds_balancer"
        },
        {
          "value": "0.33",
          "key": "osd_heartbeat_min_healthy_ratio"
        },
        {
          "value": "25",
          "key": "osd_scrub_chunk_max"
        },
        {
          "value": "/var/lib/ceph/mds/myceph-gravel1",
          "key": "mds_data"
        },
        {
          "value": "4194304",
          "key": "rgw_obj_stripe_size"
        },
        {
          "value": "0",
          "key": "osd_pool_default_flags"
        },
        {
          "value": "0",
          "key": "mds_kill_link_at"
        },
        {
          "value": "1",
          "key": "client_tick_interval"
        },
        {
          "value": "5",
          "key": "mon_tick_interval"
        },
        {
          "value": "0/5",
          "key": "rbd"
        },
        {
          "value": "1440",
          "key": "mds_blacklist_interval"
        },
        {
          "value": "524288000",
          "key": "osd_client_message_size_cap"
        },
        {
          "value": "",
          "key": "ms_inject_delay_type"
        },
        {
          "value": "false",
          "key": "clog_to_syslog"
        },
        {
          "value": "0",
          "key": "mds_kill_openc_at"
        },
        {
          "value": "4194304",
          "key": "rgw_get_obj_max_req_size"
        },
        {
          "value": "false",
          "key": "osd_auto_mark_unfound_lost"
        },
        {
          "value": "15",
          "key": "ms_max_backoff"
        },
        {
          "value": "myceph",
          "key": "cluster"
        },
        {
          "value": "15",
          "key": "osd_recovery_max_active"
        },
        {
          "value": "true",
          "key": "rgw_copy_obj_progress"
        },
        {
          "value": "false",
          "key": "rgw_enable_ops_log"
        },
        {
          "value": "",
          "key": "monmap"
        },
        {
          "value": "1099511627776",
          "key": "mds_max_file_size"
        },
        {
          "value": "true",
          "key": "osd_open_classes_on_start"
        },
        {
          "value": "",
          "key": "heartbeat_file"
        },
        {
          "value": "false",
          "key": "mon_osd_auto_mark_in"
        },
        {
          "value": "false",
          "key": "mon_sync_debug"
        },
        {
          "value": "false",
          "key": "mds_standby_replay"
        },
        {
          "value": "32",
          "key": "mon_osd_max_split_count"
        },
        {
          "value": "-1",
          "key": "mds_standby_for_rank"
        },
        {
          "value": "500",
          "key": "osd_map_cache_size"
        },
        {
          "value": "5",
          "key": "heartbeat_interval"
        },
        {
          "value": "90",
          "key": "mds_dir_max_commit_size"
        },
        {
          "value": "0.2",
          "key": "mds_bal_min_start"
        },
        {
          "value": "0",
          "key": "ms_inject_socket_failures"
        },
        {
          "value": "900",
          "key": "rgw_keystone_revocation_interval"
        },
        {
          "value": "16777216",
          "key": "rbd_cache_target_dirty"
        },
        {
          "value": "3600",
          "key": "auth_service_ticket_ttl"
        },
        {
          "value": "0",
          "key": "mds_bal_idle_threshold"
        },
        {
          "value": "false",
          "key": "osd_pool_default_flag_hashpspool"
        },
        {
          "value": "0.97",
          "key": "osd_failsafe_full_ratio"
        },
        {
          "value": "5",
          "key": "client_caps_release_delay"
        },
        {
          "value": "-1",
          "key": "mon_sync_debug_leader"
        },
        {
          "value": "false",
          "key": "ms_bind_ipv6"
        },
        {
          "value": "0/5",
          "key": "client"
        },
        {
          "value": "true",
          "key": "filestore_fail_eio"
        },
        {
          "value": "30",
          "key": "rgw_opstate_ratelimit_sec"
        },
        {
          "value": "209715200",
          "key": "client_oc_size"
        },
        {
          "value": "180",
          "key": "filestore_op_thread_suicide_timeout"
        },
        {
          "value": "10",
          "key": "filestore_max_inline_xattrs_xfs"
        },
        {
          "value": "10",
          "key": "osd_backfill_retry_interval"
        },
        {
          "value": "33554432",
          "key": "mon_leveldb_write_buffer_size"
        },
        {
          "value": "10",
          "key": "mds_bal_target_removal_max"
        },
        {
          "value": "0.1",
          "key": "mds_bal_min_rebalance"
        },
        {
          "value": "0",
          "key": "osd_leveldb_block_size"
        },
        {
          "value": "64",
          "key": "rgw_md_log_max_shards"
        },
        {
          "value": "1/5",
          "key": "rgw"
        },
        {
          "value": "false",
          "key": "fuse_debug"
        },
        {
          "value": "8388608",
          "key": "osd_recovery_max_chunk"
        },
        {
          "value": "1/5",
          "key": "asok"
        },
        {
          "value": "",
          "key": "rgw_ops_log_socket_path"
        },
        {
          "value": "false",
          "key": "rbd_cache_writethrough_until_flush"
        },
        {
          "value": "10",
          "key": "mon_client_ping_interval"
        },
        {
          "value": "true",
          "key": "clog_to_monitors"
        },
        {
          "value": "false",
          "key": "rgw_intent_log_object_name_utc"
        },
        {
          "value": "60",
          "key": "mon_sync_timeout"
        },
        {
          "value": "0",
          "key": "mds_thrash_exports"
        },
        {
          "value": "0.3",
          "key": "mon_osd_min_up_ratio"
        },
        {
          "value": "1/5",
          "key": "mon"
        },
        {
          "value": "1000",
          "key": "client_oc_max_objects"
        },
        {
          "value": "30",
          "key": "osd_mon_heartbeat_interval"
        },
        {
          "value": "466b2ff9-970e-44a4-85d1-db0718a0c836",
          "key": "fsid"
        },
        {
          "value": "6",
          "key": "osd_pgp_bits"
        },
        {
          "value": "8388608",
          "key": "osd_copyfrom_max_chunk"
        },
        {
          "value": "5",
          "key": "mds_scatter_nudge_interval"
        },
        {
          "value": "false",
          "key": "mds_debug_frag"
        },
        {
          "value": "0",
          "key": "mds_log_segment_size"
        },
        {
          "value": "0",
          "key": "mds_skip_ino"
        },
        {
          "value": "192.168.18.1,192.168.18.2,192.168.18.3",
          "key": "mon_host"
        },
        {
          "value": "0",
          "key": "osd_recovery_delay_start"
        },
        {
          "value": "0.3",
          "key": "mon_osd_min_in_ratio"
        },
        {
          "value": "0.8",
          "key": "mds_bal_need_min"
        },
        {
          "value": "0",
          "key": "mds_thrash_fragments"
        },
        {
          "value": "4194304",
          "key": "ms_pq_max_tokens_per_priority"
        },
        {
          "value": "1048576",
          "key": "rgw_copy_obj_progress_every_bytes"
        },
        {
          "value": "0/5",
          "key": "optracker"
        },
        {
          "value": "107374182400",
          "key": "osd_max_object_size"
        },
        {
          "value": "0",
          "key": "mon_sync_requester_kill_at"
        },
        {
          "value": "1",
          "key": "osd_debug_drop_pg_create_duration"
        },
        {
          "value": "2",
          "key": "mds_default_dir_hash"
        },
        {
          "value": "false",
          "key": "mon_leveldb_compression"
        },
        {
          "value": "0.85",
          "key": "osd_backfill_full_ratio"
        },
        {
          "value": "5",
          "key": "osd_recovery_max_single_start"
        },
        {
          "value": ".rgw.root",
          "key": "rgw_zone_root_pool"
        },
        {
          "value": "2",
          "key": "filestore_max_inline_xattrs_other"
        },
        {
          "value": "false",
          "key": "filestore_debug_verify_split"
        },
        {
          "value": "5",
          "key": "filestore_max_sync_interval"
        },
        {
          "value": "1000",
          "key": "mds_bal_merge_rd"
        },
        {
          "value": "5",
          "key": "mds_tick_interval"
        },
        {
          "value": "",
          "key": "rgw_script_uri"
        },
        {
          "value": "false",
          "key": "rbd_cache_block_writes_upfront"
        },
        {
          "value": "0/1",
          "key": "objecter"
        },
        {
          "value": "1/5",
          "key": "heartbeatmap"
        },
        {
          "value": "600",
          "key": "osd_command_thread_timeout"
        },
        {
          "value": "true",
          "key": "journal_dio"
        },
        {
          "value": "00000000-0000-0000-0000-000000000000",
          "key": "osd_uuid"
        },
        {
          "value": "6800",
          "key": "ms_bind_port_min"
        },
        {
          "value": "1/3",
          "key": "journal"
        },
        {
          "value": "10",
          "key": "mon_delta_reset_interval"
        },
        {
          "value": "localhost",
          "key": "host"
        },
        {
          "value": "1",
          "key": "paxos_propose_interval"
        },
        {
          "value": "500",
          "key": "filestore_wbthrottle_btrfs_inodes_start_flusher"
        },
        {
          "value": "true",
          "key": "filestore_btrfs_clone_range"
        },
        {
          "value": "auth",
          "key": "rgw_swift_auth_entry"
        },
        {
          "value": "5",
          "key": "osd_op_log_threshold"
        },
        {
          "value": "true",
          "key": "mon_osd_adjust_heartbeat_grace"
        },
        {
          "value": "3",
          "key": "rbd_default_features"
        },
        {
          "value": "1000",
          "key": "log_max_new"
        },
        {
          "value": "250",
          "key": "paxos_service_trim_min"
        },
        {
          "value": "info",
          "key": "clog_to_syslog_level"
        },
        {
          "value": "3",
          "key": "mds_bal_sample_interval"
        },
        {
          "value": "info",
          "key": "mon_cluster_log_to_syslog_level"
        },
        {
          "value": "true",
          "key": "err_to_stderr"
        },
        {
          "value": "false",
          "key": "filestore_zfs_snap"
        },
        {
          "value": "10",
          "key": "filestore_max_inline_xattrs_btrfs"
        },
        {
          "value": "",
          "key": "osd_rollback_to_cluster_snap"
        },
        {
          "value": "true",
          "key": "rgw_cache_enabled"
        },
        {
          "value": "0",
          "key": "journal_write_header_frequency"
        },
        {
          "value": "4194304",
          "key": "rbd_default_stripe_unit"
        },
        {
          "value": "false",
          "key": "rbd_cache"
        },
        {
          "value": "false",
          "key": "err_to_syslog"
        },
        {
          "value": "REMOTE_ADDR",
          "key": "rgw_remote_addr_param"
        },
        {
          "value": "false",
          "key": "journal_force_aio"
        },
        {
          "value": "32",
          "key": "rgw_gc_max_objs"
        },
        {
          "value": "",
          "key": "mds_standby_for_name"
        },
        {
          "value": "25165824",
          "key": "rbd_cache_max_dirty"
        },
        {
          "value": "86400",
          "key": "osd_scrub_min_interval"
        },
        {
          "value": "60",
          "key": "osd_scrub_thread_timeout"
        },
        {
          "value": "0",
          "key": "filestore_index_retry_probability"
        },
        {
          "value": "10",
          "key": "client_notify_timeout"
        },
        {
          "value": "0",
          "key": "osd_pool_default_crush_rule"
        },
        {
          "value": "true",
          "key": "rgw_enforce_swift_acls"
        },
        {
          "value": "false",
          "key": "rbd_balance_snap_reads"
        },
        {
          "value": "/usr/lib/rados-classes",
          "key": "osd_class_dir"
        },
        {
          "value": "1000",
          "key": "rgw_curl_wait_timeout_ms"
        },
        {
          "value": "100",
          "key": "osd_map_share_max_epochs"
        },
        {
          "value": "0/1",
          "key": "filer"
        },
        {
          "value": "10",
          "key": "mon_slurp_timeout"
        },
        {
          "value": "",
          "key": "rgw_request_uri"
        },
        {
          "value": "1000",
          "key": "mds_client_prealloc_inos"
        },
        {
          "value": "false",
          "key": "rbd_localize_snap_reads"
        },
        {
          "value": "10000",
          "key": "rgw_cache_lru_size"
        },
        {
          "value": "gravel1, gravel2, gravel3",
          "key": "mon_initial_members"
        },
        {
          "value": "8",
          "key": "osd_pool_default_pgp_num"
        },
        {
          "value": "10",
          "key": "mds_bal_interval"
        },
        {
          "value": "5",
          "key": "mds_bal_target_removal_min"
        },
        {
          "value": "false",
          "key": "fuse_use_invalidate_cb"
        },
        {
          "value": "0",
          "key": "mds_shutdown_check"
        },
        {
          "value": "false",
          "key": "mds_debug_scatterstat"
        },
        {
          "value": "2",
          "key": "osd_pool_default_size"
        },
        {
          "value": "0",
          "key": "client_readahead_max_bytes"
        },
        {
          "value": "500",
          "key": "filestore_queue_committing_max_ops"
        },
        {
          "value": "1/5",
          "key": "perfcounter"
        },
        {
          "value": "100000",
          "key": "mds_cache_size"
        },
        {
          "value": "419430400",
          "key": "filestore_wbthrottle_btrfs_bytes_hard_limit"
        },
        {
          "value": "",
          "key": "filestore_dump_file"
        },
        {
          "value": "s3, swift, swift_auth, admin",
          "key": "rgw_enable_apis"
        },
        {
          "value": "104857600",
          "key": "ms_dispatch_throttle_bytes"
        },
        {
          "value": "false",
          "key": "osd_debug_skip_full_check_in_backfill_reservation"
        },
        {
          "value": "0.95",
          "key": "mon_osd_full_ratio"
        },
        {
          "value": "64",
          "key": "osd_backfill_scan_min"
        },
        {
          "value": "",
          "key": "nss_db_path"
        },
        {
          "value": "0",
          "key": "rgw_op_thread_suicide_timeout"
        },
        {
          "value": "20",
          "key": "mds_log_max_expiring"
        },
        {
          "value": "",
          "key": "restapi_log_level"
        },
        {
          "value": "10000",
          "key": "mds_bal_split_size"
        },
        {
          "value": "500",
          "key": "filestore_wbthrottle_btrfs_ios_start_flusher"
        },
        {
          "value": "false",
          "key": "mds_wipe_ino_prealloc"
        },
        {
          "value": "true",
          "key": "mds_log"
        },
        {
          "value": "30",
          "key": "osd_client_watch_timeout"
        },
        {
          "value": "65536",
          "key": "ms_pq_min_cost"
        },
        {
          "value": "1",
          "key": "rgw_usage_max_user_shards"
        },
        {
          "value": "50",
          "key": "filestore_queue_max_ops"
        },
        {
          "value": "",
          "key": "rgw_region"
        },
        {
          "value": "-1",
          "key": "mds_bal_max"
        },
        {
          "value": "true",
          "key": "cephx_sign_messages"
        },
        {
          "value": "0.5",
          "key": "mds_dir_commit_ratio"
        },
        {
          "value": "cephx",
          "key": "auth_service_required"
        },
        {
          "value": "3",
          "key": "mon_client_hunt_interval"
        },
        {
          "value": "false",
          "key": "rgw_resolve_cname"
        },
        {
          "value": "63",
          "key": "osd_client_op_priority"
        },
        {
          "value": "45",
          "key": "mds_reconnect_timeout"
        },
        {
          "value": "false",
          "key": "osd_leveldb_paranoid"
        },
        {
          "value": "604800",
          "key": "osd_deep_scrub_interval"
        },
        {
          "value": "10",
          "key": "osd_heartbeat_min_peers"
        },
        {
          "value": "2",
          "key": "osd_op_threads"
        },
        {
          "value": "3",
          "key": "mon_lease_renew_interval"
        },
        {
          "value": "1",
          "key": "osd_crush_chooseleaf_type"
        },
        {
          "value": "true",
          "key": "mds_use_tmap"
        },
        {
          "value": "30",
          "key": "osd_op_complaint_time"
        },
        {
          "value": "128",
          "key": "rgw_data_log_num_shards"
        },
        {
          "value": "false",
          "key": "ms_die_on_old_message"
        },
        {
          "value": "",
          "key": "auth_supported"
        },
        {
          "value": "100",
          "key": "rgw_thread_pool_size"
        },
        {
          "value": "100",
          "key": "mon_globalid_prealloc"
        },
        {
          "value": "false",
          "key": "filestore_fiemap"
        }
      ]
"""
def ClusterConfig(){return;}
